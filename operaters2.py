a=20
b=-20
c=0
if a>0 or b>0:
    print("Either of the numbers is greater")
else:
    print("No number is greater than zero")


a=20
b=12
c=0
if a and b and c:
    print("All the numbers haveboolean value as True")
else:
    print("Atleast one number has boolean value as False")



a=20
b=10
c=10
print(a!=b)
print(b!=c)
a="1st no."
b="2nd no."
if a!=b:
    print(a,"and",b,"are different.")
a=4
b=5
if(a==1)!=(0==5):
    print("Hello")
a=int(input("Enter A Number: "))
if a%2!= 0:
    print(a,"is not even number")


height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))

BMI=weight/(height/100)**2
print("Your BMI is",BMI)
if BMI<=18.4:
    print("You are underweight.")
elif BMI<=24.9:
    print("You are healthy.")
elif BMI<=29.9:
    print("You are overweight.")
elif BMI<=34.9:
    print("You are severely overweight.")
elif BMI<=39.9:
    print("You are obese.")
else:
    print("You are severely obese.")
