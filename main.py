import csv
from airport import Airport
from flight import Flight 
from flight_map import FlightMap 
from flight_path import FlightPathBroken 
from flight_path import FlightPathDuplicate 
from flight_path import FlightPath 


flight_map = FlightMap()
flight_map.import_airports("aeroports.csv")
flight_map.import_flights("flights.csv")

all_airports = flight_map.airports()
all_flights = flight_map.flights()
print("")
print("--------------------- Code existe ? ---------------------")
start_airport = flight_map.airport_find("CDG")
end_airport = flight_map.airport_find("JFK")
print("")
print("--------------------- Vol trouvé ---------------------")
flight_found = flight_map.flight_find("CDG", "FRA")
# flight_map.flight_exist("CDG", "JFK")
print("")
print("--------------------- Vol avec code impliqué ---------------------")
cdg_flights = flight_map.flights_where("CDG")
# lhr_flights = flight_map.flights_where("LOS")
print("")
print("--------------------- destination pour les vols ---------------------")
cdg_destinations = flight_map.airports_from("CDG")
# lhr_destinations = flight_map.airports_from("LHR")
print("")
print("---------------------")

# Créer le chemin de voyage avec l'aéroport de départ et ajouter le premier vol
path = FlightPath(start_airport)
path.add(end_airport, flight_found)

#print(path.flights())  # [cdg_jfk_flight]
flights = path.flights()
for flight in flights:
    print(flight)
# print(path.airports())  # [start_airport, end_airport]
print("---------------------")
airports = path.airports()
for airports in airports:
    print(airports)
print("--------Etape-------------")
print(path.steps())  # 1
print("----------Durée-----------")
print(path.duration())  # duration of cdg_jfk_flight




# Recherche des plans de vols entre l'aéroport de départ et l'aéroport de destination
src_airport_code = "CDG"
dst_airport_code = "JFK"
paths = flight_map.paths(src_airport_code, dst_airport_code)

# Affichage des plans de vols trouvés
print(f"Plans de vols trouvés entre {src_airport_code} et {dst_airport_code}:")
for path in paths:
    print(f"Distance : {path.distance}")
    for flight in path.path:
        print(f"  {flight.src_code} -> {flight.dst_code} ({flight.duration}h)")