'''
instance method
class method
static method


'''

class Student:
    school = "techsrijan"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def add(self):
        return(self.m1+self.m2+self.m3)

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
       print("Running  nothing to do with class nor with instastance variable")

s1=Student(20,30,40)
s2=Student(50,60,70)

print(s1.add())

print(s2.add())

print(Student.get_school())

Student.info()