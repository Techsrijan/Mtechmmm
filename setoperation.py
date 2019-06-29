fruit={'apple','banana'}
print(fruit)
fruit.add('mango')
print(fruit)
s=  frozenset([1,2,4])
print(s)
#s.add(5)
num= {1,3,2,5,3,5,5}
print(num)
emptyset ={}
print(type(emptyset))
empty = set()
print(type(empty))
empty=set(num)
print(empty)
set1={1,2,3,4,5}
print(id(set1))
print(2 in set1)
print(6 is not set1)
set1.add(6)
print(set1)
print(6 is set1)
print(id(set1))
set1.remove(6)
print(set1)
a= {1,2,3}
b={4,5,6,3}
#union
print(a|b)
#intersection
print(a&b)
#difference
print(a-b)
print(b-a)
#symmatric difference--whic are not common in a and b
print(a^b)
print(len(a))
c=a.copy()
print(c)
a.clear()
print(a)
for i in b:
    print(i)

