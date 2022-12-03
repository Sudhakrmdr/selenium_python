class Allemployee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.sal = salary

    def dispaly(self):
        print(self.id, self.name, self.sal)


emp_one = Allemployee("Manjo", 10, 10000)
emp_two = Allemployee("Khan", 11, 10000)
# emp_three = Allemployee("Chitra", 11, 20000)
#
#
emp_one.dispaly()
emp_two.dispaly()
# emp_three.dispaly()


# class Nonparamconst:
#     def __init__(self):
#         print("iam non param constructor")
#
#     def display(self, name):
#         print("hi", name)


# obj_nonparam = Nonparamconst()
# obj_nonparam2 = Nonparamconst()
# obj_nonparam3 = Nonparamconst()
# obj_nonparam.display("sdsdsd")
