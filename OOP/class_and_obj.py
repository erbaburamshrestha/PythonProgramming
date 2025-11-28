class Animal:
    #list of attributes
    name = "baburam"
    age = 45
    address = "Kathmandu"
    color = "black"
    weight = 70
    height = 5.7

    #list of methods
    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")
    
    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Color: {self.color}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} ft")
#creating object of the class
anim = Animal()
#accessing attributes
print(anim.name)
print(anim.age)
