
#class_name.method_name call that class method no matter if it is parent
#class method or not


class base:
    def __init__(self):
        print ("base class")

class inter_base_1(base):
    def __init__(self):
        base.__init__(self)
        print ("inter base 1 class")


class inter_base_2(base):
    def __init__(self):
        base.__init__(self)
        print ("inter base 2 class")


class child(inter_base_1,inter_base_2):
    def __init__(self):
        inter_base_1.__init__(self)
        inter_base_2.__init__(self)
        print ("child class")


if __name__ == "__main__":
    c1 = child()
