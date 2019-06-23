try:
    age = int(input("enter your age"))
    if age<=0:
        raise ValueError("Age Can't be less than zero")
    print(age)
except ValueError as error:
    print(error)

