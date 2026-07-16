name="Jhon Doe"
age=25
gender='Male'

# print("Hello",name,"your age is",age,"and gender is",gender)
# print("Hello " + name + " your gender is "+gender + "your age is "+age)  

# we will get error for "your age is" + age   part beacuse  age is a integer and we can not add string + integer


# print(name,age,gender,sep="-")  # by default separator is space
# print(name,end=" ")
# print(age,end=" ")
# print(gender)

# F-Strings, format
print(f"Your name is {name}, age is {age+50} years and gender is {gender}")
print(age)
