x=list(range(10))
#print(range(10))
print(x)

y=list(range(2,10))
#print(range(10))
print(y)

z=list(range(3,40,3))
#print(range(10))
print(z)


p=list(range(300,40,-10))
#print(range(10))
print(p)

lst=[2,5,3,8,7,6,5,55]
print(lst)
a=len(lst)
print(a)
print("Length=",len(lst))

for i in range(a):
    print(lst[i])

i=0
while i<=a-1:
    print(lst[i])
    i=i+1

for p in range(1,101):
    if(p%3==0):
        print(p)