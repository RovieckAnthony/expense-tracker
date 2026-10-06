print("========================================")
print("             EXPENSE TRACKER")
print("       Know where your money goes.")
print("========================================")
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

exp2_name = input("Second expense? ")
exp2_amount = float(input("Amount? "))

tax_rate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

subtotal = exp1_amount + exp2_amount
average = subtotal / 2
tax_amount = subtotal * (tax_rate / 100)
grand_total = subtotal + tax_amount
over_budget = grand_total > budget
left_in_budget = budget - grand_total

print()
print("-" * 40)
print("SUMMARY")
print(f"- {exp1_name}:    ${exp1_amount}")
print(f"- {exp2_name}:     ${exp2_amount}")
print(f"Subtotal:    ${subtotal}")
print(f"Average:     ${average}")
print(f"Tax ({tax_rate}%):    ${tax_amount}")
print(f"Grand total: ${grand_total}")
print(f"Over budget? {over_budget}")
print(f"Left in budget: ${left_in_budget}")
print("-" * 40)
print("Made by: Rovieck Anthony Ramos  |  Installment 3")