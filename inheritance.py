class animal:
    ismammal = True
    gender = "male"
    age = 2

    def movement(self):
        print("animal is moving")

class cow(animal):
    def moow(self):
        print("cow is moowing")

class cat(animal):
    def meow(self):
        print("cat is meowing")

mycow = cow()
mycow.moow()

mycat = cat()
mycat.meow()