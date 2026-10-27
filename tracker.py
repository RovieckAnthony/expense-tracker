print("=" * 44)
print("              EXPENSE TRACKER               ")
print("        Know where your money goes.         ")
print("=" * 44)
print()

name = input("What's your name? ")
tax_rate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")
print()

expense_count = 0
subtotal = 0.0

while True:
    print("MAIN MENU")
    print("[1] Add an expense")
    print("[2] View all expenses      (coming soon)")
    print("[3] Show total spent")
    print("[4] Exit")
    
    choice = input("Choose 1-4: ")
    print()
    
    if choice == "1":
        amount = float(input("Amount? "))
        expense_count += 1
        subtotal += amount
        if amount <= 50:
            print("  Small expense.")
        else:
            print("  Big expense.")
        print()
        
    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")
        print()
        
    elif choice == "3":
        tax_amount = subtotal * (tax_rate / 100)
        grand_total = subtotal + tax_amount
        remaining = budget - grand_total
        
        print("EXPENSES:", expense_count)
        print(f"Subtotal:       ${subtotal:.1f}")
        print(f"Tax ({tax_rate:.1f}%):    ${tax_amount:.1f}")
        print(f"Grand total:    ${grand_total:.1f}")
        print(f"Careful: only ${remaining:.1f} left.")
        print()
        
    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 44)
        print("Made by: Rovieck Anthony Ramos | Installment 5")
        break
        
    else:
        print("Please choose 1, 2, 3 or 4.")
        print()