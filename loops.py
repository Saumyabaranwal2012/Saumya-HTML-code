n=int(input("ENTER NUMBER WHOSE SUM YOU WANT TO FIND: "))
sum=0
for i in range(1, n+1):
    sum=sum+i
    print("\n Sum=", sum)


string=input("ENTER THE STRING YOU WANT TO REVERSE: ")
string2=('')
for i in string:
        string2=i+string2
print("\nThe original string: ",string)
print("The reversed string: ",string2)


n=int(input("Enter the value: "))
print("numbers from {0} to {1} are: ".format(n,1))
for i in range(n,0,-1):
        print(i)