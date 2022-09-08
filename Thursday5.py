bank_total = 300
deposit_money = 40
withdraw_money = 140

# if deposit_money is greater than 0
if deposit_money > 0:
    bank_total = bank_total + deposit_money
    print(f"New bank total  : £ {bank_total}")
else:
    print("Invalid deposit total!")

# if withdraw_money is less than or equal to bank_total
if withdraw_money <= bank_total:
    if withdraw_money >= 0:
        bank_total = bank_total - withdraw_money
        print(f"After withdrawing £ {withdraw_money}, the new total is £ {bank_total}")
    else:
        print("Invalid withdraw amount!")
else:
    print(f"Invalid withdraw amount of £ {withdraw_money}, not enough funds")








# if withdraw_money >0 then minus from total


# new_total

# else not enough in the bank account