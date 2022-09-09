"""

def timesthreeplus9(num):
    print(num * 3 + 9)


timesthreeplus9(6)

"""


# greeting method definition


def greeting(name, age):
    print(f"Hello, my name is {name} and I am {str(age)} years old.")


# the user is prompted to enter both a name and age
username = input("Please enter a name ")
userage = input("Please enter an age ")

# the print function then calls the greeting method
greeting(username, userage)
