class Circle:
    #Apparently python doesn't support multiple constructors
    def __init__(self, radius:float = 1.0, color:str = "red"):
        self.__radius = radius
        self.__color = color

    def getRadius(self) -> float:
        return self.__radius

    def setRadius(self, radius: float) -> None:
        self.__radius = radius

    def getColor(self) -> str:
        return self.__color

    def setColor(self, color:str) -> None:
        self.__color = color
    
    def toString(self) -> str:
        #Not really clear what the question is asking for here
        return str(self.__radius)
    
    def getArea(self) -> float:
        return 3.1416 * (self.__radius ** 2)

class Cylinder(Circle):
    def __init__(self, height: float = 1.0, radius: float = 1.0, color: str = "red"):
        Circle.__init__(self, radius, color)
        self.__height = height

    def getHeight(self) -> float:
        return self.__height

    def setHeight(self, height: float) -> None:
        self.__height = height

    def toString(self) -> str:
        #Not really clear what the question is asking for here
        return str(self.__height)
    
    def getVolume(self) -> float:
        return self.__height*self.getArea()
