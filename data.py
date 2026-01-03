#lets check the datatype
a=29
print("type of a:",type(a))

b=2.9
print("type of b:",type(b))

c="Python"
print("type of c:",type(c))

d=True
print("type of d:",type(d))


#assigning different variables
name="Penguin"
age=14
is_student=True
weight=45.5

#printing variables and data types
print("name:",name)
print("Data type of name is:",type(name))

print("Age:",age)
print("Data type of age is:",type(age))

print("is_student:",is_student)
print("Data type of is_student is:",type(is_student))

print("weight:",weight)
print("Data type of weight is:",type(weight))

#type casting
print("\n After type casting...")

age=str(age)
print(age)
print("Data type of age is:",type(age))

weight=int(weight)
print(weight)
print("Data type of weight is:",type(weight))

#input a word
text=str(input("Enter a string:"))

#reverse string
#using value-1 to write in reverse
revText= text[::-1]
text= revText

print("Reverse of given string is:")
print(text)