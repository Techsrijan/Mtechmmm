class A:
    def msg_a(self):
        print("I am class a Method")


class B:
    def msg_b(self):
        print("I am class b Method")

class C(A,B) :
    def display(self):
        self.msg_a()
        self.msg_b()


S= C()
S.display()