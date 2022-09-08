"""
    A simple weight conversion program from K to lbs
    but using .lower to ensure less code
___________________________________________________
"""

weight = float(input("Please enter a weight : "))
selection = input("(K)g or (L)bs : ")

if selection.lower() == "k":
    print(f"Weight in Lbs : {weight * 2.205} ")
elif selection.lower() == "l":
    print(f"Weight in Lbs : {weight / 2.205} ")
else:
    print("Not a valid selection")
