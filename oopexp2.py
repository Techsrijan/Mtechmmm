class Student:
    def data(self):
        print("abc",33,'samsung')



#to create an object
st=Student()
st1=Student()

print(type(st))
#every object has new memory space
print(id(st))
print(id(st1))

st.data()
st1.data()

Student.data(st)