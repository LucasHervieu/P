class Flight:
    def __init__(self, src_code: str="", dst_code: str="", duration: float=0):
        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration
    def __str__(self) -> str:
        # retourne une chaîne de caractères représentant l'objet Flight
        return f"src_code: {self.src_code} dst_code: {self.dst_code} duration: {self.duration}"