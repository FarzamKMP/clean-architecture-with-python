# ============================================================
# 🧩 SOLID Principles in Python
# ============================================================
# SOLID represents 5 key design principles for writing clean,
# maintainable, and scalable object-oriented software.
#
# S - Single Responsibility
# O - Open/Closed
# L - Liskov Substitution
# I - Interface Segregation
# D - Dependency Inversion
# ============================================================


# ============================================================
# 1️⃣ S - Single Responsibility Principle (SRP)
# ------------------------------------------------------------
# A class should have only one reason to change.
# Each class should focus on a single responsibility or purpose.
# ============================================================

# ❌ Bad Example — Multiple responsibilities in one class
class Report:
    def generate(self):
        print("Generating report...")

    def save_to_file(self):
        print("Saving to file...")

    def send_email(self):
        print("Sending via email...")

# ✅ Good Example — Split responsibilities into separate classes
class Report:
    def generate(self):
        print("Generating report...")

class FileSaver:
    def save(self, report):
        print("Saving report to file...")

class EmailSender:
    def send(self, report):
        print("Sending report via email...")

# Usage Example
report = Report()
report.generate()
FileSaver().save(report)
EmailSender().send(report)



# ============================================================
# 2️⃣ O - Open/Closed Principle (OCP)
# ------------------------------------------------------------
# Software entities should be open for extension but closed for modification.
# You should be able to add new functionality without changing existing code.
# ============================================================

# ❌ Bad Example — Every time a new payment method is added, we modify this class
class PaymentProcessor:
    def pay(self, method):
        if method == "paypal":
            print("Paying with PayPal")
        elif method == "credit":
            print("Paying with Credit Card")

# ✅ Good Example — Use inheritance and polymorphism for extension
class PaymentMethod:
    def pay(self):
        pass

class PayPal(PaymentMethod):
    def pay(self):
        print("Paying with PayPal")

class CreditCard(PaymentMethod):
    def pay(self):
        print("Paying with Credit Card")

class PaymentProcessor:
    def process(self, payment: PaymentMethod):
        payment.pay()

# Usage Example
processor = PaymentProcessor()
processor.process(PayPal())
processor.process(CreditCard())



# ============================================================
# 3️⃣ L - Liskov Substitution Principle (LSP)
# ------------------------------------------------------------
# Subclasses should be replaceable with their base classes
# without breaking the behavior of the program.
# ============================================================

# ❌ Bad Example — Ostrich breaks the behavior of Bird
class Bird:
    def fly(self):
        print("Flying...")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly!")  # Violates LSP

# ✅ Good Example — Redefine hierarchy properly
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying...")

class Ostrich(Bird):
    def run(self):
        print("Running fast!")

# Usage Example
eagle = FlyingBird()
eagle.fly()

ostrich = Ostrich()
ostrich.run()



# ============================================================
# 4️⃣ I - Interface Segregation Principle (ISP)
# ------------------------------------------------------------
# Clients should not be forced to depend on methods they do not use.
# Split large interfaces into smaller, specific ones.
# ============================================================

# ❌ Bad Example — Robot must implement "eat" even if it doesn’t need it
class Worker:
    def work(self): pass
    def eat(self): pass

class Robot(Worker):
    def work(self): print("Robot working...")
    def eat(self): pass  # Pointless implementation

# ✅ Good Example — Split into separate interfaces
class Workable:
    def work(self): pass

class Eatable:
    def eat(self): pass

class Human(Workable, Eatable):
    def work(self):
        print("Human working...")
    def eat(self):
        print("Human eating...")

class Robot(Workable):
    def work(self):
        print("Robot working...")

# Usage Example
Human().work()
Human().eat()
Robot().work()



# ============================================================
# 5️⃣ D - Dependency Inversion Principle (DIP)
# ------------------------------------------------------------
# High-level modules should not depend on low-level modules.
# Both should depend on abstractions (interfaces).
# ============================================================

# ❌ Bad Example — Switch depends directly on LightBulb
class LightBulb:
    def turn_on(self):
        print("Light on")

    def turn_off(self):
        print("Light off")

class Switch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb

    def operate(self, on):
        if on:
            self.bulb.turn_on()
        else:
            self.bulb.turn_off()

# ✅ Good Example — Depend on abstractions, not implementations
class Switchable:
    def turn_on(self): pass
    def turn_off(self): pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Light on")

    def turn_off(self):
        print("Light off")

class Fan(Switchable):
    def turn_on(self):
        print("Fan on")

    def turn_off(self):
        print("Fan off")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self, on):
        if on:
            self.device.turn_on()
        else:
            self.device.turn_off()

# Usage Example
bulb_switch = Switch(LightBulb())
fan_switch = Switch(Fan())

bulb_switch.operate(True)
fan_switch.operate(False)



# ============================================================
# ✅ Summary
# ------------------------------------------------------------
# S - Single Responsibility → One class, one purpose.
# O - Open/Closed → Extend behavior without modifying existing code.
# L - Liskov Substitution → Subclasses must behave like their parents.
# I - Interface Segregation → Smaller, focused interfaces are better.
# D - Dependency Inversion → Depend on abstractions, not concrete classes.
# ============================================================