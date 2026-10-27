
# Expense Tracker - Installment 4: tracker makes decisions

print("=" * 40)

print("            EXPENSE TRACKER")
print("        Track your spending with ease.")

print("=" * 40)

print()

print("MAIN MENU")
print("  [1] Add an expense            (coming soon)")
print("  [2] View all expenses         (coming soon)")
print("  [3] Show total spent          (coming soon)")
print("  [4] Exit                      (coming soon)")

print()

name = input("What's your name? ")

print(f"Welcome, {name}! Let's log two expenses.")

print()

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

subtotal = subtotal + amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

subtotal = subtotal + amount2

if amount1 > 100 and amount2 > 100:
    print("Two big expenses in a row - slow down!")

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)

total = subtotal + tax

budget = float(input("Your budget? "))

over_budget = total > budget
left = budget - total

print()

print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:     ${amount1}")
print(f"  - {item2}:      ${amount2}")
print(f"Subtotal:       ${subtotal}")
print(f"Average:        ${average}")
print(f"Tax ({tax_percent}%):    ${tax}")
print(f"Grand total:    ${total}")

if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total > budget * 0.9:
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")

print("-" * 40)

print(f"Made by: {name}  |  Installment 4")
