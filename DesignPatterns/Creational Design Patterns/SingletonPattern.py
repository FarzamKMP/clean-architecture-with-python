# ============================================================
# 🧩 Singleton Pattern
# Ensures a class has only one instance and provides a global access point.
# بعضی چیزها تو برنامه فقط باید یه دونه وجود داشته باشن — مثلاً تنظیمات (config)، دیتابیس، logger و غیره.
# ============================================================

class Singleton:
    _instance = None  # Holds the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Creating the single instance...")
        return cls._instance


# Usage Example
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # ✅ True — both are the same instance