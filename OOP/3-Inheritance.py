class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} makes sound")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} makes sound")

cat = Cat("Lucy")
cat.speak()
dog = Dog("Bob")
dog.speak()