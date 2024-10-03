from ICalcGeo import ICalcGeo

class Rectangle(ICalcGeo):

    def __init__(self,longueur:int=1,largeur:int=1)->None:
        """
        Constructeur de la classe Rectangle.
        Args:
            longueur:int
            largeur:int
        """

        # Les propriétés
        self.__longueur=longueur #self._Rectangle__longueur
        self.__largeur=largeur
    
    @property
    def longueur(self)->int:
        """
        """
        return self.__longueur
    @property
    def largeur(self)->int:
        """
        """
        return self.__largeur

    @longueur.setter
    def longueur(self,longueur):
        if longueur<=0:
            raise Exception('longueur<=0')
        self.__longueur =longueur
    
    @largeur.setter
    def largeur(self,largeur):
        if largeur<=0:
            raise Exception('largeur<=0')
        self.__largeur =largeur
    
    def get_surface(self):
        return self.__largeur*self.__longueur
    
    def __str__(self) -> str:
        return f"Rectangle {self.__largeur=}, {self.__longueur=}"
    
    # 
    def __eq__(self, value: object) -> bool:
        if isinstance(value,__class__):        
            return self.__longueur == value.__longueur and self.__largeur == value.__largeur
        else:
            raise Exception("Hooooooo !")
    
    # longueur = property(get_longueur,set_longueur,doc="La doc de longueur")
    # largeur = property(get_largeur,set_largeur,doc="La doc de largeur")