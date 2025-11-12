# ============================================================
# 🧩 Adapter Pattern
# Converts the interface of one class into another that a client expects.
#سازگار کردن دو کلاس که با هم سازگار نیستن.
# فرض کن دو کلاس داری که باید با هم کار کنن،
# ولی یکی از متدهاش اسم یا ساختار متفاوتی داره — Adapter به عنوان یه “مترجم” بینشون عمل می‌کنه.
# ============================================================

class EuropeanSocket:
    def voltage(self): return 230
    def live(self): return 1
    def neutral(self): return -1

class USASocket:
    def voltage(self): return 120
    def live(self): return 1
    def neutral(self): return -1

# Adapter connects a European device to a USA socket
class EuropeanToUSAdapter:
    def __init__(self, european_socket):
        self.socket = european_socket

    def voltage(self):
        # Convert 230V to 120V
        return 120

    def live(self):
        return self.socket.live()

    def neutral(self):
        return self.socket.neutral()

# Usage Example
euro_socket = EuropeanSocket()
adapter = EuropeanToUSAdapter(euro_socket)
print("Voltage after adaptation:", adapter.voltage())  # ✅ 120