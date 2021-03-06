class Company():
    def __init__(self, name: str, cars: list):
        """
        name: prints the name of the company
        cars: a list of 'Car' objects that this company manufactures
        """
        self.name = name
        self.car = cars

class Car():
    def __init__(self, model:str, speed:int, tank_capacity:float, fuel_usage:float):
        """ 
        model: the name/model of the car
        speed: average speed in km/h
        tank_capacity: max capacity of the gas tank in Liters
        fuel_usage: gas used in liters/100km

        """
        self.model = model
        self.speed = speed
        self.tank_capacity = tank_capacity
        self.fuel_usage = fuel_usage

    def max_distance(self) -> float:
        """ calculates the maximum distance the car can run """
        return self.tank_capacity / self.fuel_usage

    def max_duration(self) -> float:
        """ calculates how many minutes the car can go """
        return self.max_distance() / self.speed

    def is_better_than(self, other_car : Car) -> str:
        """ compares if this car is better than another """
        if self.max_distance() > other_car.max_distance() and self.max_duration() > other_car.max_duration():
            return "yes"
        elif self.max_distance() > other_car.max_distance() or self.max_duration() > other_car.max_duration():
            return "maybe"
        else:
            return "no"

    def compare_cars(self, other_company: Company) -> None:
        count = 0
        for i in other_company.cars:
            if self.is_better_than(other_company.cars[i]):
                count += 1
        print(f"Our car, {self.model} is better than {count} out of {len(other_company.cars)} in their company") 


car1 = Car("Model S", 50, 37, 8.5)
car2 = Car("Model 3", 45, 40, 10.2)
car3 = Car("Model X", 55, 46, 7.9)

car4 = Car("Rock", 50, 45, 9.4)

company1 = Company("Tebsla", [car1, car2, car3])

print(car4.is_better_than(car1)) # Prints "yes"
print(car2.is_better_than(car3)) # Prints "no"
print(car1.is_better_than(car2)) # Prints "maybe"