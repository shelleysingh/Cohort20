# dictionary

sauron = {"name": "Sauron", "no_rings": 1, "ring_missing": True, "address": "Mordor", "popularity": -1.025}
print(type(sauron))
print(sauron)

gandalf = {"name": "Gandalf", "ring_missing": False}

print(gandalf)
print(type(gandalf))

gandalf["no_rings"] = 1
gandalf["address"] = "none"
gandalf["popularity"] = 98.27

print(gandalf)

print("if statement version")
if "address" in sauron:
    print(sauron["address"])
else:
    print("Sauron does not have an address")

print("try block version")
try:
    print(sauron["address"])
except KeyError:
    print("Sauron does not have an address")

for key in gandalf.keys():
    value = gandalf[key]
    print(key, "=", value)
