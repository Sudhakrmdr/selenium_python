# list_of_course = ["Python", "git", "selenium", "jira", "alm", 10, 25.5, True, False]
# print(list_of_course)
# print(type(list_of_course))
#
# print("length of the string", len(list_of_course))
#
# print("Access specific iteam", list_of_course[2])

# Negative index: Start from the end
# print("Access specific iteam", list_of_course[-1])

# list_of_course = ["Python", "git", "selenium", "jira", "alm", 10, 25.5, True, False, 45454,5656, "Khan"]
# Start - include
# end = exclude
# print("Range of the elements", list_of_course[2:5])
# print("Range of the elements", list_of_course[4:6])

# print("Range of the elements", list_of_course[5:])

# print("Range of the elements", list_of_course[:5])

# list_of_states_in_usa = ["TX", "AZ", "CA", "WA"]
# if "TG" in list_of_states_in_usa:
#     print("Yes, element is present")x`x`

# changing a specific elem
# list_of_states_in_usa = ["TX", "AZ", "CA", "WA"]
#
# list_of_states_in_usa[1] = "NY"
# print(list_of_states_in_usa)

# insert the other states in to your list
# list_of_states_in_usa = ["TX", "AZ", "CA", "WA"]
#
# # list_of_states_in_usa.insert(3, "TX")
# #
# # print(list_of_states_in_usa)
#
# list_of_states_in_usa.append("MA")
# print(list_of_states_in_usa)

# fruit_one = ["mange", "banana", "grapes"]
# fruit_two = ["papaya", "pineapple", "orange"]
# fruit_one.extend(fruit_two)
# print(fruit_one)

# fruit_one = ["mange", "banana", "grapes"]
# fruit_two = ("papaya", "pineapple", "orange", "orange", "orange")
# fruit_one.extend(fruit_two)
# print(fruit_one)

# fruit_one = ["mange", "banana", "grapes", "papaya"]
# fruit_one.sort()
# print(fruit_one)

fruit_one = [12, 2, 45, -1, 23]
# fruit_one.sort()
# print(fruit_one)
# fruit_one.reverse()
# print(fruit_one)
x = fruit_one.pop(1)
print(x)