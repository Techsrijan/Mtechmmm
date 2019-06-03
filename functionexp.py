def greet():
    print("Good Morning")
    print("thank You")


greet()
greet()

def sum(x,y):
    c=x+y
    print(c)

sum(10,10)


def addtwo(p,q):
    m = p+q
    return m

s = addtwo(4,6)
print(s)

def calci(x,y):
    a = x+y
    b = x-y
    c = x*y
    return a,b,c

r,s,t=calci(40,5)
print("Sum=",r,"Sub=",s,"Multi=",t)

def person(name,age=18):
    print("Name=",name,"age=",age)
    age=age+10
    print(age)

#position
person("ABCD",25)
#person(35,"hum")

#keyword
person(name="ashwani",age=44)
person(age=44,name="asas")
'''
actual argument can pass in a function 
1. Position
2. Keyword
3. Default
4. Variable length argument
'''

#Default
person(name="humtum")
person(name="ashwani",age=44)

# variable length

def sumvarible(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)

sumvarible(2,3,5,6,6,8,36,6,63,69,6)


def sumvarible1(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
sumvarible1(2,3,5,6,6,8,36,6,63,69,6)

def personinfo(name,*data):
    print(name)
    print(data)

personinfo('ram',33,'mumbai',9956477677)

#keyword vraiblelength argument
def personinfo1(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

personinfo1('abcd',age=32,city='delhi',phone=9956477677)
