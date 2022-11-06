
# While
# while expressions:
#     statements

count=0
while count < 10:
    print(count)
    count +=1

i = 10
while i > 0:
    print(i)
    i -= 1


count=0
while count < 10:
    print(count)
    count +=2

print("Good by")

count=0
while count < 10:
    print(count)
    count +=1
    if (count == 6):
        print(count)
        break

# sum of squares
i = 1
sum = 0
while i < 10:
    print(i ** 2)
    sum = i ** 2 + sum
    i +=1
print("Sum of the squares", sum)


# tables
# 1 * 2 = 2
# 2 * 2 = 4

i = 1
table_num = 8998
while i <= 10:
    j = i * table_num
    print(str(i) + "*" + str(table_num) + " = " + str(j))
    i += 1


