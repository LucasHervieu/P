class Airport:
    def __init__(self, name: str ="", airport_code: str="", lat: float=0, long: float=0):
        self.name = name
        self.code = airport_code
        self.lat = lat
        self.long = long
    def __str__(self) -> str:
        # retourne une chaîne de caractères représentant l'objet Airport
        return f"{self.name} ({self.code}), lat={self.lat}, long={self.long}"