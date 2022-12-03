class BOA:
    def roi(self):
        print("BOA 10")

class WF(BOA):
    def roi(self):
        print("WF 19")

obj_ref = WF()
obj_ref.roi()

obj_bo = BOA()
obj_bo.roi()
