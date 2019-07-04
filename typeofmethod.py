'''
instance method
class method
static method


'''
class Student:
    school = "techsrijan"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def add(self):
        return (self.m1 + self.m2 + self.m3)

    @classmethod  #decorator
    def get_Schoolname(cls):
        return cls.school

    @staticmethod
    def msg():
        print("nothing to do with instance method or class method")



s1=Student(20,30,40)
s2=Student(50,60,70)

print(s1.add())

print(s2.add())

print(Student.get_Schoolname())

Student.msg()

