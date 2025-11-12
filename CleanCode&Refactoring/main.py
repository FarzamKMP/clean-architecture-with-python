# ============================================================
# 🧹 Clean Code & Refactoring Examples in Python
# ------------------------------------------------------------
# Goal: Transform code that "works" into code that is "well written".
# We'll cover:
# - Naming conventions
# - Function size (Single purpose)
# - Comments & readability
# - DRY (Don't Repeat Yourself)
# - KISS (Keep It Simple, Stupid)
# - YAGNI (You Ain’t Gonna Need It)
# ============================================================


# ============================================================
# 1️⃣ Naming — Use meaningful, descriptive names
# ============================================================

# ❌ Bad Example
def f(a, b):
    return a * b / 2

result = f(10, 5)
print(result)  # What does this do???

# ✅ Good Example
def calculate_triangle_area(base, height):
    """Calculate area of a triangle using formula (base * height) / 2"""
    return base * height / 2

area = calculate_triangle_area(10, 5)
print("Triangle area:", area)


# ============================================================
# 2️⃣ Function Size — One function = One responsibility
# ============================================================

# ❌ Bad Example: Doing too many things at once
def process_user(data):
    # validate
    if not data.get("email"):
        raise ValueError("Missing email")
    # save to DB
    print(f"Saving {data['email']} to database...")
    # send email
    print(f"Sending welcome email to {data['email']}")

process_user({"email": "test@example.com"})


# ✅ Good Example: Split into smaller, focused functions
def validate_user(data):
    if not data.get("email"):
        raise ValueError("Missing email")

def save_user_to_db(data):
    print(f"Saving {data['email']} to database...")

def send_welcome_email(data):
    print(f"Sending welcome email to {data['email']}")

def process_user_refactored(data):
    validate_user(data)
    save_user_to_db(data)
    send_welcome_email(data)

process_user_refactored({"email": "test@example.com"})


# ============================================================
# 3️⃣ Comments — Explain WHY, not WHAT
# ============================================================

# ❌ Bad Example: Useless comments
# This function returns x + y
def add(x, y):
    return x + y

# ✅ Good Example: Explain intent or tricky logic
def calculate_discount(price, customer_type):
    """
    Apply discount based on customer type.
    VIP customers get 20%, regular get 10%.
    """
    discount_rate = 0.2 if customer_type == "VIP" else 0.1
    return price * (1 - discount_rate)


# ============================================================
# 4️⃣ DRY — Don't Repeat Yourself
# ============================================================

# ❌ Bad Example: Repeating logic
def pay_with_credit(amount):
    print(f"Processing credit payment of {amount}")
    print("Connecting to bank...")
    print("Payment successful!")

def pay_with_paypal(amount):
    print(f"Processing PayPal payment of {amount}")
    print("Connecting to bank...")
    print("Payment successful!")

# ✅ Good Example: Extract common logic
def process_payment(method, amount):
    print(f"Processing {method} payment of {amount}")
    print("Connecting to bank...")
    print("Payment successful!")

process_payment("credit", 100)
process_payment("paypal", 50)


# ============================================================
# 5️⃣ KISS — Keep It Simple, Stupid
# ============================================================

# ❌ Bad Example: Overengineering simple logic
def is_even(num):
    # Using unnecessary conditions
    if num % 2 == 0:
        return True
    else:
        return False

# ✅ Good Example: Simpler is better
def is_even_clean(num):
    return num % 2 == 0


# ============================================================
# 6️⃣ YAGNI — You Ain’t Gonna Need It
# ============================================================

# ❌ Bad Example: Adding unused features
class ReportGenerator:
    def __init__(self):
        self.format = "PDF"
        self.enable_encryption = True  # Not used anywhere!

    def generate(self, data):
        print("Generating PDF report...")

# ✅ Good Example: Only implement what you actually need
class SimpleReport:
    def generate(self, data):
        print("Generating simple report...")

report = SimpleReport()
report.generate("Sales data")


# ============================================================
# ✅ Summary
# ------------------------------------------------------------
# - Use clear, meaningful names
# - Keep functions small and focused
# - Write comments for WHY, not WHAT
# - Avoid repetition (DRY)
# - Simplicity over cleverness (KISS)
# - Don’t build features you don’t need (YAGNI)
# ============================================================