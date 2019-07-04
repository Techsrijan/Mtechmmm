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