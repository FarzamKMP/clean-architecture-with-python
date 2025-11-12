# ============================================================
# 🧩 Strategy Pattern
# Allows selecting an algorithm's behavior at runtime.
# رفتار (الگوریتم) قابل تعویض در زمان اجرا
# به جای اینکه چند if/else برای انتخاب رفتار بنویسی،
# رفتارها رو در کلاس‌های جدا تعریف کن و در زمان اجرا تصمیم بگیر از کدوم استفاده بشه.
# ============================================================

class PaymentStrategy:
    def pay(self, amount):
        pass

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount}$ using PayPal.")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount}$ using Credit Card.")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount}$ using Bitcoin.")

# Context
class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)

# Usage Example
cart1 = ShoppingCart(PayPalPayment())
cart1.checkout(50)

cart2 = ShoppingCart(BitcoinPayment())
cart2.checkout(120)