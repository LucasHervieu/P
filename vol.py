# import csv
# from collections import deque

# class Airport:
#     def __init__(self, name: str ="", airport_code: str="", lat: float=0, long: float=0):
#         self.name = name
#         self.code = airport_code
#         self.lat = lat
#         self.long = long
#     def __str__(self) -> str:
#         # retourne une chaîne de caractères représentant l'objet Airport
#         return f"{self.name} ({self.code}), lat={self.lat}, long={self.long}"
# # paris_charles_de_gaulle = Airport("Paris Charles de Gaulle", "CDG", 49.012779, 2.55)
# class Flight:
#     def __init__(self, src_code: str="", dst_code: str="", duration: float=0):
#         self.src_code = src_code
#         self.dst_code = dst_code
#         self.duration = duration
#     def __str__(self) -> str:
#         # retourne une chaîne de caractères représentant l'objet Flight
#         return f"src_code: {self.src_code} dst_code: {self.dst_code} duration: {self.duration}"



# class FlightPathBroken(Exception):
#     pass

# class FlightPathDuplicate(Exception):
#     pass


# class FlightPath:
#     def __init__(self, src_airport: Airport):
#         self.__airports = [src_airport]
#         self.__flights = []

#     def add(self, dst_airport: Airport, via_flight: Flight) -> None:
#         if self.__airports[-1].code != via_flight.src_code: 
#             raise FlightPathBroken(f"Error : le vol de {via_flight.src_code} à {via_flight.dst_code} n'a pas de correspondance avec l'aéroport {self.__airports[-1].code}")
#         if dst_airport in self.__airports:  
#             raise FlightPathDuplicate(f"Error : l'aéroport {dst_airport.code} est déjà présent dans le chemin")
#         self.__airports.append(dst_airport)
#         self.__flights.append(via_flight)

#     def flights(self) -> list[Flight]:
#         return self.__flights

#     def airports(self) -> list[Airport]:
#         return self.__airports

#     def steps(self) -> int:
#         return len(self.__airports) - 1

#     def duration(self) -> float:
#         duration = 0
#         for flight in self.__flights:
#             duration += flight.duration
#         return duration

# class FlightMap:
#     def __init__(self):
#         self.__airports = []
#         self.__flights = []

#     def import_airports(self, csv_file: str) -> None:
#         with open(csv_file, "r") as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 name, code, lat, long = row
#                 code = code.replace('"', '').replace(' ', '')  # nettoyage du code de l'aéroport
#                 lat, long = float(lat.strip(' "')), float(long.strip(' "'))  # nettoyage des coordonnées de l'aéroport
#                 self.__airports.append(Airport(name, code, lat, long))

#     def import_flights(self, csv_file: str) -> None:
#         with open(csv_file, "r") as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 src_code, dst_code, duration = row
#                 src_code = src_code.replace('"', '').replace(' ', '')  # nettoyage du code de l'aéroport
#                 dst_code = dst_code.replace('"', '').replace(' ', '')  # nettoyage du code de l'aéroport
#                 duration = float(duration)
#                 self.__flights.append(Flight(src_code, dst_code, duration))

#     def airports(self) -> list[Airport]:
#         return self.__airports

#     def flights(self) -> list[Flight]:
#         return self.__flights

#     def airport_find(self, airport_code: str) -> tuple[bool, Airport]:
#         for airport in self.__airports:
#             if airport.code == airport_code:
#                 print(f"Success : Aéroport avec le code {airport_code} trouvé")
#                 return airport

#         print(f"Error : Aéroport avec le code {airport_code} est introuvable")
#         return None
        
#     def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
#         return bool(self.flight_find(src_airport, dst_airport_code))

#     def flight_find(self, src_airport_code: str, dst_airport_code: str) -> Flight:
#         for flight in self.__flights:
#             if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code:
#                 print(f"Success: vol trouvé de {src_airport_code} à {dst_airport_code}")
#                 return flight
                
#         print(f"Error: Pas de vol trouvé de {src_airport_code} à {dst_airport_code}")
#         return None

#     def flights_where(self, airport_code: str) -> list[Flight]:
#         flights = []
#         for flight in self.__flights:
#             if flight.src_code == airport_code or flight.dst_code == airport_code:
#                 flights.append(flight)
#         if not flights:
#             print(f"Error: Aucun vol trouvé impliquant l'aéroport {airport_code}")
#         else:
#             print(f"Success: {len(flights)} vol(s) trouvé impliquant l'aéroport {airport_code}")
#         return flights

#     def airports_from(self, airport_code: str) -> list[Airport]:
#         airports = []
#         for flight in self.__flights:
#             if flight.src_code == airport_code:
#                 dst_airport = self.airport_find(flight.dst_code)
#                 if dst_airport:
#                     airports.append(dst_airport)
#         if not airports:
#             print(f"Error: Aucune destination trouvée pour les vols au départ de {airport_code}")
#         else:
#             print(f"Success: {len(airports)} destinations trouvées pour les vols au départ de {airport_code}")
#         return airports 
#     def paths(self, src_airport_code: str, dst_airport_code: str) -> list[FlightPath]:
#         # Initialisation de la liste des aéroports non visités et des aéroports futurs
#         airports_not_visited = self.__airports[:]
#         airports_future = deque()

#         # Initialisation de la liste des aéroports visités et du premier aéroport à visiter
#         airports_visited = []
#         airports_future.append(src_airport_code)

#         # Initialisation de la liste des plans de vols trouvés
#         paths = []

#         # Tant qu'il y a encore des aéroports à visiter
#         while airports_future:
#             # Récupération du prochain aéroport à visiter
#             airport_code = airports_future.popleft()

#             # Si l'aéroport est déjà visité, on passe au suivant
#             if airport_code in airports_visited:
#                 continue

#             # Ajout de l'aéroport aux aéroports visités
#             airports_visited.append(airport_code)

#             # Si l'aéroport est l'aéroport de destination, on ajoute un plan de vol à la liste
#             if airport_code == dst_airport_code:
#                 paths.append(FlightPath([], 0))
#                 continue

#             # Recherche des aéroports accessibles depuis l'aéroport actuel
#             for flight in self.__flights:
#                 if flight.src_code == airport_code:
#                     # Ajout de l'aéroport destination à la liste des aéroports futurs
#                     airports_future.append(flight.dst_code)

#                     # Création d'un nouveau plan de vol en ajoutant le vol actuel au plan de vol précédemment trouvé
#                     new_path = FlightPath(paths[-1].path + [flight], paths[-1].distance + 1)
#                     paths.append(new_path)

#         # Retour de la liste des plans de vols trouvés
#         return paths









# flight_map = FlightMap()
# flight_map.import_airports("aeroports.csv")
# flight_map.import_flights("flights.csv")

# all_airports = flight_map.airports()
# all_flights = flight_map.flights()
# print("")
# print("--------------------- Code existe ? ---------------------")
# start_airport = flight_map.airport_find("CDG")
# end_airport = flight_map.airport_find("JFK")
# print("")
# print("--------------------- Vol trouvé ---------------------")
# flight_found = flight_map.flight_find("CDG", "FRA")
# # flight_map.flight_exist("CDG", "JFK")
# print("")
# print("--------------------- Vol avec code impliqué ---------------------")
# cdg_flights = flight_map.flights_where("CDG")
# # lhr_flights = flight_map.flights_where("LOS")
# print("")
# print("--------------------- destination pour les vols ---------------------")
# cdg_destinations = flight_map.airports_from("CDG")
# # lhr_destinations = flight_map.airports_from("LHR")
# print("")
# print("---------------------")

# # Créer le chemin de voyage avec l'aéroport de départ et ajouter le premier vol
# path = FlightPath(start_airport)
# path.add(end_airport, flight_found)

# #print(path.flights())  # [cdg_jfk_flight]
# flights = path.flights()
# for flight in flights:
#     print(flight)
# # print(path.airports())  # [start_airport, end_airport]
# print("---------------------")
# airports = path.airports()
# for airports in airports:
#     print(airports)
# print("--------Etape-------------")
# print(path.steps())  # 1
# print("----------Durée-----------")
# print(path.duration())  # duration of cdg_jfk_flight




# # Recherche des plans de vols entre l'aéroport de départ et l'aéroport de destination
# src_airport_code = "CDG"
# dst_airport_code = "JFK"
# paths = flight_map.paths(src_airport_code, dst_airport_code)

# # Affichage des plans de vols trouvés
# print(f"Plans de vols trouvés entre {src_airport_code} et {dst_airport_code}:")
# for path in paths:
#     print(f"Distance : {path.distance}")
#     for flight in path.path:
#         print(f"  {flight.src_code} -> {flight.dst_code} ({flight.duration}h)")