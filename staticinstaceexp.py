'''

Namespace is an area where you can create or store object/variable.
 1 class namespace
 2. object/instance namespace

'''

class Car:
    wheel =555 # static or class variable we do not need object
    def __init__(self):
        self.name='Maruti'   #here name and mil are instance variable
        self.mil=25


print(Car.wheel)
#print(Car.name)
omni=Car()
omni.mil=18
print(omni.name,omni.mil,omni.wheel)
desire=Car()
desire.name="swift"
print(desire.name,desire.mil,Car.wheel)