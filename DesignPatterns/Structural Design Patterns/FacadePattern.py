# ============================================================
# 🧩 Facade Pattern
# Provides a simple interface to a complex subsystem.
#فراهم کردن یک رابط ساده‌تر برای یک سیستم پیچیده.
# گاهی یک سیستم از چندین کلاس و متد تشکیل شده
# ولی کاربر فقط یه متد ساده می‌خواد برای انجام کل کار.
# Facade مثل یه “واسط دوستانه” است که پشتش چندین کار انجام میشه.
# ============================================================

class CPU:
    def freeze(self): print("Freezing CPU...")
    def jump(self, position): print(f"Jumping to {position}...")
    def execute(self): print("Executing instructions...")

class Memory:
    def load(self, position, data):
        print(f"Loading data {data} into position {position}...")

class HardDrive:
    def read(self, lba, size):
        return f"Data from sector {lba} (size {size})"

# Facade hides complexity
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        print("Starting computer...")
        self.cpu.freeze()
        data = self.hard_drive.read(0, 100)
        self.memory.load(0, data)
        self.cpu.jump(0)
        self.cpu.execute()

# Usage Example
computer = ComputerFacade()
computer.start_computer()
