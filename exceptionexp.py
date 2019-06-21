a=10
b=2
lst= [1,2,3]
print("I opened th freez")
try:
    d=a/b
    print(d)
    print(lst[1])
    #print("Thank you")
except IndexError as e:
    print("you are accress the out of range element")
    #print("Thank you")
except ZeroDivisionError  as e:
    print("ba can not be zero")
    #print("Thank you")
except Exception as e:
    print("pagla gaye ho ka",e)
    #print("Thank you")
finally:
    print("Freez is closed")
