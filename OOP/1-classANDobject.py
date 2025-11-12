class Dog:
    def __init__(self, name, breed): # Attribute (ویژگی)
        self.name = name
        self.breed = breed

    def bark(self): # Method (رفتار)
        print(f"{self.name} says woof!")

dog1 = Dog("Bob", "Golden Retriever")
dog1.bark()
dog2 = Dog("Luna", "Husky")
dog2.bark()