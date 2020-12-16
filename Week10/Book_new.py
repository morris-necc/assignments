from Author import *

class Book:
    def __init__(self, name: str, author: [Author], price: float):
        self.__name = name
        self.__author = author
        self.__price = price

    def __init__(self, name: str, authors: [Author], price: float, qty: int = 0):
        self.__name = name
        self.__authors = authors
        self.__price = price
        self.__qty = qty

    def getName(self) -> str:
        return self.__name
    
    def getAuthors(self) -> [Author]:
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
        def author_helper() -> str:
            """Helps printing out all the author toString methods"""
            authors_info = ""
            for author in self.__authors:
                authors_info += f"{author.toString()},"
            return "{"+authors_info[:-1]+"}"

        return f"Book[name={self.__name},authors={author_helper()},price={self.__price},qty={self.__qty}]"

    def getAuthorNames(self) -> str:
        authors = ""
        for author in self.__authors:
            authors += f"{author.getName()},"
        return authors[:-1]

# Next slide's testing
bob = Author("Bob", "bob@gmail.com", "m")
dave = Author("Dave", "dave@gmail.com", "m")
biography = Book("What it's like to be named Bob", [bob, dave], 15.0, 1)

print(biography.toString())
print(biography.getAuthorNames())