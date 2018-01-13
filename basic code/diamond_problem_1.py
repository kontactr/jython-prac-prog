class a1:
    def __init__(self):
        print ("a1")

class a(a1):
    def __init__(self):
        super().__init__()
        print ("a")

class b(a1):
    def __init__(self):
        super().__init__()
        print ("b")

class c(a):
    def __init__(self):
        super().__init__()
        print ("c")

class d(b):
    def __init__(self):
        super().__init__()
        print ("d")

class e(c,d):
    def __init__(self):
        super().__init__()
        print ("e")



f = e()
