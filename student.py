from re import L


class Student:
    # name = 'Kanini'
    # age = 30
    # country = 'Kenya'
    school = 'Akirachix'
    def __init__(self,firstname, lastname, age,country):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
    def greet(self):
        return f"Hello {self.name} from {self.country}, welcome to the {self.school}"
    def fullname(self):
       return self.firstname + " " + self.lastname
    
    def year_of_birth(self):
        return 2022- self.age
    
    def initals(self):
        return self.firstname[0].upper() + self.lastname[0].upper()