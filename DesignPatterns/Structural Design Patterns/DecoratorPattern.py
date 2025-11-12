# ============================================================
# 🧩 Decorator Pattern
# Dynamically adds behavior to an object at runtime.
# اضافه کردن رفتار جدید به یک شیء بدون تغییر در ساختار اصلی آن.
# فرض کن یه کلاس داری و می‌خوای قابلیت‌های بیشتری بهش بدی
# (مثل log کردن، امنیت، کش، و غیره) بدون اینکه اون کلاس تغییر کنه.
# اینجا Decorator وارد میشه.
# ============================================================

class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

# Usage Example
coffee = Coffee()
print("Plain Coffee:", coffee.cost())

milk_coffee = MilkDecorator(coffee)
print("With Milk:", milk_coffee.cost())

sweet_milk_coffee = SugarDecorator(milk_coffee)
print("With Milk + Sugar:", sweet_milk_coffee.cost())