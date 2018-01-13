
#super always ref to parent object and call next methods 


class base:
    def __init__(self):
        print ("base class")


class inter_base_1(base):
    def __init__(self):
        super().__init__()
        print ("inter base 1 class")


class inter_base_2(base):
    def __init__(self):
        super().__init__()
        print ("inter base 2 class")


class child(inter_base_1,inter_base_2):
    def __init__(self):
        super().__init__()
        print ("child class")


if __name__ == "__main__":
    c1 = child()
