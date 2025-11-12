# ============================================================
# 🧩 Builder Pattern
# Step-by-step construction of complex objects.
# ساخت اشیاء پیچیده رو گام‌به‌گام انجام بده.
# وقتی یه کلاس تعداد زیادی پارامتر داره یا ساختش چند مرحله‌ایه، از Builder استفاده کن.
# ============================================================

class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None

    def __str__(self):
        return f"Computer(cpu={self.cpu}, gpu={self.gpu}, ram={self.ram})"


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self, cpu):
        self.computer.cpu = cpu
        return self  # allows chaining

    def add_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def add_ram(self, ram):
        self.computer.ram = ram
        return self

    def build(self):
        return self.computer


# Usage Example
builder = ComputerBuilder()
computer = builder.add_cpu("Intel i9").add_gpu("NVIDIA RTX 4090").add_ram("64GB").build()
print(computer)
