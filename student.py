class Student:
    # name = 'Kanini'
    # age = 30
    # country = 'Kenya'
    school = 'Akirachix'
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country
    def greet(self):
        return f"Hello {self.name} from {self.country}, welcome to the {self.school}"
    def otherCredentials(self, firstName, lastName, initials, year_of_birth):
        self.firstName = firstName
        self.lastName = lastName
        self.initials = initials
        self.year_of_birth = year_of_birth
