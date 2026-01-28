number=int(input("Enter A Number: "))
if number>0:
    print("The Number Is Positive")
elif number<0:
    print("The Number Is Negative")
else:
    print("The Number Is Zero")


actualcost=float(input("Please Enter The Actual Item price: "))
actualsale=float(input("Please Enter The Actual Sale Price: "))
if(actualsale > actualcost):
    amount=actualsale-actualcost
    print("Total profit=",format(amount))
else:
    print("No Profit!!!!!")


inputno=int(input("Please Enter The 1st Number: "))
inputn=int(input("Please Enter The 2nd Number: "))
if(inputno>inputn):
    input=inputno
    print("The Greatest Number is: ",format(input))
else:
    print("The Greatest Number is The Second Number ")


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
