import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name 
        self.country = country
        self.dob = dob

    def calculate_age(self):
        today = datetime.datetime.today()
        age = today.year - self.dob.year
        return age


dob = datetime.datetime(2002, 10, 31)

person = Person("Tejesh", "India", dob)   

print(f"Age of {person.name} is {person.calculate_age()}")
