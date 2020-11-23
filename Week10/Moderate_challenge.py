class Person:
    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address

    def getName(self) -> str:
        return self.__name
    
    def getAddress(self) -> str:
        return self.__address

    def setAddress(self, address: str) -> None:
        self.__address = address

    def toString(self) -> str:
        return self.__name+"("+self.__address+")"

class Student(Person):
    def __init__(self, name: str, address: str):
        Person.__init__(self, name, address)
        self.__numCourses = 0
        #Not sure if the following 2 are supposed to be arrays or dictionaries
        self.__courses = {}
        self.__grades = {}

    def toString(self):
        #Since they didn't specify what to do with this method
        return super().toString()

    def addCourseGrade(self, course: str, grade: int) -> None:
        #Not really sure what this function does with the variables
        #Enters courses by alphabetical order
        if course not in self.__courses:
            self.__courses[course[0]] = [course]
        else:
            self.__courses[course[0]].append(course)
        
        #Enters grades by course
        if course not in self.__grades:
            self.__grades[course] = [grade]
        else:
            self.__grades[course].append(grade)

    def printGrades(self) -> None:
        for course in self.__grades:
            for grade in self.__grades[course]:
                print(grade, end = ' ')
    
    def getAverageGrade(self) -> float:
        total = 0
        iterations = 0
        for course in self.__grades:
            for grade in self.__grades[course]:
                total += grade
                iterations += 1
        return total/iterations
    
    def toString(self) -> str:
        return "Student: "+super().toString()

class Teacher(Person):
    def __init__(self, name: str, address: str):
        Person.__init__(self, name, address)
        self.__numCourses = 0
        self.__courses = {}

    def toString(self):
        #Since they didn't specify what to do with this method
        return super().toString()

    def addCourse(self, course: str) -> bool:
        try:
            if course not in self.__courses[course[0]]:
                self.__courses[course[0]].append(course)
                return True
            else:
                return False
        except:
            self.__courses[course[0]] = [course]
            return True
    
    def removeCourse(self, course: str) -> bool:
        try:
            if course in self.__courses[course[0]]:
                self.__courses[course[0]].remove(course)
                return True
            else:
                return False
        except:
            return False

    def toString(self) -> str:
        return "Teacher: "+super().toString()