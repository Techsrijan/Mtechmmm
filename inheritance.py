
'''

Deriving a new class from the base class is known as inhertitance
Room --base (Parent)
GuestRoom --Derived class (child)
type of inheritance
1. single level inhertitance
2. multilevel inheritance
3. hierarchical inheritance
4. multiple inheritance
5. Hybrid Inhritance
'''
class room:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        print("area=",self.l*self.b)


class GuestRoom(room):  #here Guest Room inherits the property
    def msg(self):
        print("guest room")
    '''
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Guest Room area=", self.l * self.b)
'''

r=room(20,30)
r.area()




r1=GuestRoom(270,30)
r1.area()
r1.msg()