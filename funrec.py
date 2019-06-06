import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
i= 0
def greet():
    print("good Morning")
    global i
    i=i+1
    print(i)
    greet()# function calls itself

greet()
