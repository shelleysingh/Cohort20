numbers = [1, 2, 3, 4, 5]
item_2 = 1
i = 0

for item in numbers:
    print(item)

print(50 * "-")

while item_2 in numbers:

    print(item_2)
    item_2 += 1

print(50 * "-")

while i < len(numbers):
    print(numbers[i])
    i += 1

print(50 * "-")

name_list = "Aidan"

for num in name_list:
    print(num)

print(50 * "-")

example = range(2, 8, 2)

for number in example:
    print(number)
