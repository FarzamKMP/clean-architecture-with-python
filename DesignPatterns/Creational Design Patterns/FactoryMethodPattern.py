# ============================================================
# 🧩 Factory Method Pattern
# Define an interface for creating an object,
# but let subclasses decide which class to instantiate.
# به جای ساخت مستقیم اشیاء با new، ساخت رو به یک کلاس دیگر (factory) بسپار.
# وقتی نمی‌خوای کلاس اصلی بدونه دقیقاً چه نوع شیئی ساخته میشه، از Factory استفاده کن.
# ============================================================

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            return None

# Usage Example
factory = ShapeFactory()
shape1 = factory.get_shape("circle")
shape2 = factory.get_shape("square")

shape1.draw()
shape2.draw()