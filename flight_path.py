from airport import Airport
from flight import Flight 
class FlightPathBroken(Exception):
    pass

class FlightPathDuplicate(Exception):
    pass


class FlightPath:
    def __init__(self, src_airport: Airport):
        self.__airports = [src_airport]
        self.__flights = []

    def add(self, dst_airport: Airport, via_flight: Flight) -> None:
        if self.__airports[-1].code != via_flight.src_code: 
            raise FlightPathBroken(f"Error : le vol de {via_flight.src_code} à {via_flight.dst_code} n'a pas de correspondance avec l'aéroport {self.__airports[-1].code}")
        if dst_airport in self.__airports:  
            raise FlightPathDuplicate(f"Error : l'aéroport {dst_airport.code} est déjà présent dans le chemin")
        self.__airports.append(dst_airport)
        self.__flights.append(via_flight)

    def flights(self) -> list[Flight]:
        return self.__flights

    def airports(self) -> list[Airport]:
        return self.__airports

    def steps(self) -> int:
        return len(self.__airports) - 1

    def duration(self) -> float:
        duration = 0
        for flight in self.__flights:
            duration += flight.duration
        return duration
