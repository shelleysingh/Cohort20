text = "HelloWorld"

print(text.count("!"))

if text.startswith("Hell"):
    print("It's Hell in there!")

if text.isalpha():
    print("This string is all alpha ")

text = "  \t\r\n"

if text.isspace():
    print("string is whitespace")
