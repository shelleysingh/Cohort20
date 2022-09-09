names = 0

print("Type the names of people one at a time")

while names <= 2:
    named_p = input(f"type the name of person number: {names + 1}")
    if named_p == "Aidan":
        continue
        print("Oh, no, anyone but Aidan!!! ")
    print(f"{named_p} is awesome")
    names += 1
print("This is the end of the program")
