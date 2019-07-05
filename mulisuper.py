class A:
    def __init__(self):
        print("I am class a Method")


class B:
    def __init__(self):
        print("I am class b Method")

class C(A,B):
    def __init__(self):
        '''

        mtehod resolution order
        always prefer left side
        '''
        super().__init__()
        print("I am class C Method")


b=C()