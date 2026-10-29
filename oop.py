class Employee:
    def __init__(self,  name, gender, position ):
        self.name = name
        self.gender = gender
        self.position = position

    def movement(self):
        print("Employee is walking")

employee1 = Employee(name="Marry", gender="F", position="CEO")
print(employee1.name)
employee1.movement()

employee2 = Employee(name="John", gender="M", position="Secretary")

employee3 = Employee(name="John", gender="M", position="CEO")

employee4 = Employee(name="John", gender="M", position="Secretary")




