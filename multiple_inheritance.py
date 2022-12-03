class Parent:
    def name(self):
        print("printing Parent class values")


class ParentTwo:
    def car(self):
        print("mom plz give me a car")

    def flight(self):
        print("mom plz give me a car")

class Child(Parent, ParentTwo):
    def salary(self):
        print("getting 1M")




obj_c = Child()
obj_c.car()
obj_c.name()
obj_c.salary()

obj = ParentTwo()
obj.car()
obj.flight()
