print("=" * 44)
print("              EXPENSE TRACKER               ")
print("        Know where your money goes.         ")
print("=" * 44)
print()
print("MAIN MENU")
print("[1] Add an expense         (coming soon)")
print("[2] View all expenses      (coming soon)")
print("[3] Show total spent       (coming soon)")
print("[4] Exit                   (coming soon)")
print()

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")
print()

exp1_name = input("First expense? ")
exp1_amount = float(input("Amount? "))
if exp1_amount <= 50:
    print("  Small expense.")
else:
    print("  Big expense.")

exp2_name = input("Second expense? ")
exp2_amount = float(input("Amount? "))
if exp2_amount <= 50:
    print("  Small expense.")
else:
    print("  Big expense.")

tax_rate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

subtotal = exp1_amount + exp2_amount
average = subtotal / 2
tax_amount = subtotal * (tax_rate / 100)
grand_total = subtotal + tax_amount
remaining = budget - grand_total

print("-" * 44)
print("SUMMARY")
print(f"  - {exp1_name.capitalize()}:      ${exp1_amount:.1f}")
print(f"  - {exp2_name.capitalize()}:      ${exp2_amount:.1f}")
print(f"Subtotal:       ${subtotal:.1f}")
print(f"Average:        ${average:.1f}")
print(f"Tax ({tax_rate:.1f}%):    ${tax_amount:.1f}")
print(f"Grand total:    ${grand_total:.1f}")
print(f"Careful: only ${remaining:.1f} left.")
print("-" * 44)
print("Made by: Rovieck Anthony Ramos | Installment 4")