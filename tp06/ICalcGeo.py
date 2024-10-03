from abc import ABC,abstractmethod

class ICalcGeo(ABC):

    @abstractmethod
    def get_surface(self):
        pass
    
    # def get_surface(self):
    #     raise NotImplementedError("")