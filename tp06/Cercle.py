from ICalcGeo import ICalcGeo
import math

class Cercle(ICalcGeo):
    
    def __init__(self,rayon):
        self.__rayon = rayon

    @property
    def rayon(self):
        return self.__rayon

    @rayon.setter
    def rayon(self,rayon):
        self.__rayon=rayon
    
    def get_surface(self):
        return math.pi*self.__rayon**2
        