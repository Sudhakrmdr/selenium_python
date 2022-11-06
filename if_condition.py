# if (condition):
#     #true
#     # execute this block
# else: # condition false

# Comparison operator

a = 100
b = 10
if a == b:
    print("both values are same")
elif a > b:
    print("a is bigger numbr")
elif b > a:
    print("b is bigger")

job = "working"
if job == "IT":

    print('buy a home imme')
else:
    print("probably later")


a = 20
b = 100
print(a) if a>b else print(b)
"45" - 45

input_value = input("enter a value: ")
if int(input_value) % 2 == 0:
    print("entered value is even number"+ input_value)
else:
    print("Entered value is Odd number"+ input_value)

# Logical operatior and, or, not
a, b, c = 10000, 2000, 3000
if a > b and a > c:
    print("a is bigger")
elif c > a and c > b:
    print("C is bigger")
else:
    print("b is bigger")

# OR

a, b, c = 1000, 200, 3000
if a > b or a > c:
    print("a is bigger")
    print("at least one of the conditions should be True")

# not -revers