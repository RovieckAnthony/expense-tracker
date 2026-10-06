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

total_spent = exp1_amount + exp2_amount
average = total_spent / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"- {exp1_name}:    ${exp1_amount}")
print(f"- {exp2_name}:     ${exp2_amount}")
print(f"Total spent: ${total_spent}")
print(f"Average:     ${average}")
print("-" * 40)
print("Made by: Juan Dela Cruz  |  Installment 2")