class Animal(object):
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}I am an animal")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} I am a dog")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} I am a cat")

# 4️⃣ Polymorphism (same method, different behavior)
animals = [Dog("Rocky"), Cat("Luna")]
for a in animals:
    a.speak()  # Each object runs its own version of speak()
