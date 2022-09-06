string_example = "I\'am going to\' the shops"

print(string_example)


quote_from_trek = """The line, "Beam me up scotty, was never used in Star Trek"
I'm sure you will find that this is an interesting fact"""

print(quote_from_trek)

print(50 * "-")

string_a = "Derrick"
print("The length of this string is = ", len(string_a))

print("The first element in this string is = ", string_a[0])

print("This string in upper case is = ", string_a.upper())

print("This string in lower case is = ", string_a.lower())

string_b = "Derrick, Matt, Jessica"
print(string_b)

string_c = string_b.split(",")

print("If we split all the bits of string_b up, it becomes string_c and is ", type(string_c), "and has", len(string_c), "elements" )

print(string_c)


