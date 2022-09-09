def menu():
    print(f"Please enter an option")
    print("""
    type 1 for fire lasers
    Type 2 for raise shields
    Type 3 for run away and exit the program
    """)
    choice = int(input())
    if choice == 1:
        option1()  # fire lasers
        menu()
    elif choice == 2:
        option2()  # raise shields
        menu()
    elif choice == 3:
        option3()  # run away and exit
    else:
        "You have picked an incorrect choice"
        menu()


def option1():
    print(f"Firing the lasers")


def option2():
    print("Raising the shields")


def option3():
    print("Running away - right now!")


menu()




