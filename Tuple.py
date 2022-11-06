# tup_one = ("name", 12, 12.03, False, "name")
# print(tup_one)
# print(type(tup_one))
#
# print(len(tup_one))
#
# print(tup_one[0:3])
# print(tup_one[-3:-1])

# Convert into a list
# tup_states = ("CA", "AZ", "NW")
# print(type(tup_states))
# convert_list = list(tup_states)  # convert tuple into a list
# print(type(convert_list))
# convert_list.append("KM")       # Added items to a list
# tup_states = tuple(convert_list)   # convert list into a tuple
# print(tup_states)

# Add tuple to a tuple

# tup_one = ("AZ", "MA")
# tup_two = ("CA", "AZ", "NW")
# tup_one = tup_one + tup_two
# print(tup_one)

# tup_two = ("Khan", "GE", "CA") # tuple packing - Placing the values
# (emp_name, org, state) = tup_two  # tuple Unpacking - getting  the values
# print(emp_name, org, state)

# org = ("itc", "infy", "tcs", "amazon", "ibM")
# (BANGLORE, HYD, MUM, *usa) = org
#
# print(BANGLORE)
# print(HYD)
# print(MUM)
# print(usa)


org = ("itc", "infy", "tcs", "amazon", "ibM")
tup_one = org * 2
print(tup_one)












