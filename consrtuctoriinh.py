class A:
    def __init__(self):
        print("I am class a Method")


class B(A):
    def __init__(self):
        super().__init__()
        print("I am class b Method")

class C(B):
    def __init__(self):
        super().__init__()
        print("I am class C Method")


b=C()