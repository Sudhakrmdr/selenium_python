# lambda function or abonumous functions
# lambda arguments: expression

# x = lambda a, b : a+b
# print(x(2,4))
#
# squa = lambda a: a *a
# print(squa(50))


# fliter, map

# list_one = [1,2,3,4,5,6,7,8,9]
#
# x = filter(lambda a: a>5, list_one)
# print(list(x))

# person = [("Manjot", 23),("Khan", 24),("baby", 12), ("SUdhakar", 35),("parvathi", 14)]
#
# age_to_drink = lambda age:(age[1]> 15)
#
# drinking_buddies = list(filter(lambda age:(age[1]> 15), person))
#
# # drinking_buddies = list(filter(age_to_drink,person))
# print(drinking_buddies)

# number = [1,2,3,4,5,6,7,8,9]
# even_numbers = list(filter(lambda a: a%2 == 0, number))
# print(even_numbers)

# number = [1,2,3,4,5,6,7,8,9]
# odd_numbers = list(filter(lambda a: a%2 != 0, number))
# print(odd_numbers)


# map
# map(lambda , itr)
#
# my_list = [5,4,7,9,10,23]
# new_list = map(lambda a: a**2, my_list)
# print(list(new_list))

# my_list = [5,4,7,9,10,23]
# new_list = map(lambda a: a*2, my_list)
# print(list(new_list))
#
# my_list = [5,4,7,9,10,23]
# new_list = map(lambda a: a+2, my_list)
# print(list(new_list))

my_list = [5,4,7,9,10,23]
my_list2 = [2, 3, 2, 4, 5, 2]

x = map(lambda a,b: a*b, my_list,my_list2)
print(list(x))
print(set(x))

# x = "Gmail.com"
# y = "gmail.com"
# print(id(x))
# print(id(y))


# fruit =["BanANA", "aPPLE", "GRAPES"]
# low_case_fruits = map(lambda a : a.upper(),fruit)
# print(list(low_case_fruits))


