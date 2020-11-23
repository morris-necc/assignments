class Author:
    def __init__(self, name: str, email: str, gender: str):
        self.__name = name
        self.__email = email
        self.__gender = gender
    
    def getName(self) -> str:
        return self.__name

    def getEmail(self) -> str:
        return self.__email
    
    def setEmail(self, email: str) -> None:
        self.__email = email

    def getGender(self) -> str:
        return self.__gender

    def toString(self) -> str:
        return f"Author[name={self.__name},email={self.__email},gender={self.__gender}]"
    
