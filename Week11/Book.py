from Author import *

class Book:
    def __init__(self, name: str, author: Author, price: float):
        self.__name = name
        self.__author = author
        self.__price = price

    def __init__(self, name: str, author: Author, price: float, qty: int = 0):
        self.__name = name
        self.__author = author
        self.__price = price
        self.__qty = qty

    def getName(self) -> str:
        return self.__name
    
    def getAuthor(self) -> Author:
        return self.__author
    
    def getPrice(self) -> float:
        return self.__price

    def setPrice(self, price: float) -> None:
        self.__price = price

    def getQty(self) -> int:
        return self.__qty

    def setQty(self, qty: int) -> None:
        self.__qty = qty

    def toString(self) -> str:
        return f"Book[name={self.__name},{self.__author.toString()},price={self.__price},qty={self.__qty}]"

    # Next slide's modifications
    def getAuthorName(self) -> str:
        return self.getAuthor().getName()
    
    def getAuthorEmail(self) -> str:
        return self.getAuthor().getEmail()

    def getAuthorGender(self) -> str:
        return self.getAuthor().getGender()

# Next slide's testing
bob = Author("Bob", "bob@gmail.com", "m")
bob_biography = Book("What it's like to be named Bob", bob, 15.0, 1)
print(bob_biography.getAuthor().getName(), bob_biography.getAuthor().getEmail())
