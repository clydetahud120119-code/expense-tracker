
# Expense Tracker - Installment 5: The Menu Comes Alive

print("=" * 40)
print("            EXPENSE TRACKER")
print("        Track your spending with ease.")
print("=" * 40)
print()

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print(f"Welcome, {name}!")
print()

subtotal = 0
count = 0

while True:
    print("MAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))

        subtotal = subtotal + amount
        count = count + 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total

        print(f"  {'Expenses:':<14}{count}")
        print(f"  {'Subtotal:':<14}${subtotal}")

        tax_label = f"Tax ({tax_percent}%):"
        print(f"  {tax_label:<14}${tax}")

        print(f"  {'Grand total:':<14}${total}")

        if total > budget:
            print(f"  Over budget by ${total - budget}!")
        elif total > budget * 0.9:
            print(f"  Careful: only ${left} left.")
        else:
            print(f"  Within budget. ${left} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print(f"Made by: {name}  |  Installment 5")
        print("=" * 40)
        break

    else:
        print("  Please choose 1, 2, 3 or 4.")

    print()
