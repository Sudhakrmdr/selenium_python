# for loop syntax
# for value in sequence

li = [1, 2, 4, 5, 6]

for i in li:
    print(i)


li = ("apple", "banana", 4, 5, 6)

for i in li:
    print(i)

# range(start, stop, step)
for value in range(6):
    print(value)

for value in range(4, 10):
    print(value)

# even numbers
for value in range(0, 10, 2):
    print(value)

for value in range(10, 0, -1):
    print(value)

my_dict = {1: "Khan", 2: "Khan",  3: "Manjoth"}
for i, name in my_dict.items():
    print(i)
#     print(name)
list_one = ["CA", "WT", "IL", "TX", "AZ", "FL"]
for i in list_one:
    print(i)
    if i == "IL":
        print("It's Khan's ADDA")
else:
    print("fininshed")

list_one = ["CA", "WT", "IL", "TX", "AZ", "FL"]
for i in list_one:
    print(i)
    if i == "IL":
        break
else:
    print("fininshed")


for value in list_one[1:3]:
    print(value.capitalize())

for v in "Khan":
    print(v)

# even numbers: reminder 0
tup = (2, 3, 4, 5, 6, 7, 8, 9)
for i in tup:
    if i % 2 == 0:
        print(i)

# Odd
tup = (2, 3, 4, 5, 6, 7, 8, 9)
for i in tup:
    if i % 2 != 0:
        print(i)
