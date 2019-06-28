'''

list input by user

'''
#creates an empty list
'''L= list()
print(L)
#L = list(input("enter the elements of List"))

L =eval(input("enter the elements of List"))
print(L)'''

l1=[1,2]
l2=[1,2]
l3=[1,2,3,3,3,3,[4,6]]
print(l3[3])
print(len(l3))
print("count=",l3.count(3))
print(l1==l2)

print(l2>l3)

print(l2<l3)

print(l1*3)


'''for data in L:
    print(L[data])'''
'''lst=[1,2,5,366,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
     3,3,3,3,3,3,3,3,3,33,]
print(1 is not lst )'''

'''

operator : identity operator
is return true if both operands are pointing to te same object
is not
'''
print('identity')
a =50
print(id(a))
b = 10
c=50
print(id(c))

print(a is b)

print(a is not b)

print(a is c)

print(a==c)

s1= input("enter your name")
print("S1=",s1)

s2= input("enter your name")
print("S2=",s2)

print(s1==s2)

print(s1 is s2)