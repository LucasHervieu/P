import csv
from airport import Airport
from flight import Flight 
from flight_path import FlightPath
from collections import deque


class FlightMap:
    def __init__(self):
        self.__airports = []
        self.__flights = []

    def import_airports(self, csv_file: str) -> None:
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                name, code, lat, long = row
                code = code.replace('"', '').replace(' ', '')  # nettoyage du code de l'aéroport
                lat, long = float(lat.strip(' "')), float(long.strip(' "'))  # nettoyage des coordonnées de l'aéroport
                self.__airports.append(Airport(name, code, lat, long))

    def import_flights(self, csv_file: str) -> None:
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                src_code, dst_code, duration = row
                src_code = src_code.replace('"', '').replace(' ', '')  # nettoyage du code de l'aéroport
                dst_code = dst_code.replace('"', '').replace(' ', '')  # nettoyage du code de l'aéroport
                duration = float(duration)
                self.__flights.append(Flight(src_code, dst_code, duration))

    def airports(self) -> list[Airport]:
        return self.__airports

    def flights(self) -> list[Flight]:
        return self.__flights

    def airport_find(self, airport_code: str) -> tuple[bool, Airport]:
        for airport in self.__airports:
            if airport.code == airport_code:
                print(f"Success : Aéroport avec le code {airport_code} trouvé")
                return airport

        print(f"Error : Aéroport avec le code {airport_code} est introuvable")
        return None
        
    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        return bool(self.flight_find(src_airport, dst_airport_code))

    def flight_find(self, src_airport_code: str, dst_airport_code: str) -> Flight:
        for flight in self.__flights:
            if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code:
                print(f"Success: vol trouvé de {src_airport_code} à {dst_airport_code}")
                return flight
                
        print(f"Error: Pas de vol trouvé de {src_airport_code} à {dst_airport_code}")
        return None

    def flights_where(self, airport_code: str) -> list[Flight]:
        flights = []
        for flight in self.__flights:
            if flight.src_code == airport_code or flight.dst_code == airport_code:
                flights.append(flight)
        if not flights:
            print(f"Error: Aucun vol trouvé impliquant l'aéroport {airport_code}")
        else:
            print(f"Success: {len(flights)} vol(s) trouvé impliquant l'aéroport {airport_code}")
        return flights

    def airports_from(self, airport_code: str) -> list[Airport]:
        airports = []
        for flight in self.__flights:
            if flight.src_code == airport_code:
                dst_airport = self.airport_find(flight.dst_code)
                if dst_airport:
                    airports.append(dst_airport)
        if not airports:
            print(f"Error: Aucune destination trouvée pour les vols au départ de {airport_code}")
        else:
            print(f"Success: {len(airports)} destinations trouvées pour les vols au départ de {airport_code}")
        return airports 
    
    def paths(self, src_airport_code: str, dst_airport_code: str) -> list[FlightPath]:
        # Initialisation de la liste des aéroports non visités et des aéroports futurs
        airports_not_visited = self.__airports[:]
        airports_future = deque()

        # Initialisation de la liste des aéroports visités et du premier aéroport à visiter
        airports_visited = []
        airports_future.append(src_airport_code)

        # Initialisation de la liste des plans de vols trouvés
        paths = []

        # Tant qu'il y a encore des aéroports à visiter
        while airports_future:
            # Récupération du prochain aéroport à visiter
            airport_code = airports_future.popleft()

            # Si l'aéroport est déjà visité, on passe au suivant
            if airport_code in airports_visited:
                continue

            # Ajout de l'aéroport aux aéroports visités
            airports_visited.append(airport_code)

            # Si l'aéroport est l'aéroport de destination, on ajoute un plan de vol à la liste
            if airport_code == dst_airport_code:
                paths.append(FlightPath([], 0))
                continue

            # Recherche des aéroports accessibles depuis l'aéroport actuel
            for flight in self.__flights:
                if flight.src_code == airport_code:
                    # Ajout de l'aéroport destination à la liste des aéroports futurs
                    airports_future.append(flight.dst_code)

                    # Création d'un nouveau plan de vol en ajoutant le vol actuel au plan de vol précédemment trouvé
                    new_path = FlightPath(paths[-1].path + [flight], paths[-1].distance + 1)
                    paths.append(new_path)

        # Retour de la liste des plans de vols trouvés
        return paths

