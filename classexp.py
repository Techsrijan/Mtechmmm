'''
object is an entity which can be uniquely identified in the real world;
class is a group of similar object.
class is a blueprint that represents state and behavior of the object of same kind;

class
{
object
}

class

{
state
behavior
}


class
{
 variable
 method()
 }

'''
def msg():
    print("hi")

msg()

class Computer:
    def config(self):
        print('core i3, 4 GB RAM , 1TB HDD')



#Computer.config()
#how to create object of class

comp1 = Computer()
comp2= Computer()

print(type(comp1))
#Computer.config(comp1)

comp1.config()
comp2.config()
