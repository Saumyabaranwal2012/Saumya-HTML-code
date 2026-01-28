string=input("Please enter a word: ")
char=input("Please enter a character: ")
i=0
count=0
while(i<len(string)):
    if(string[i]==char):
        count=count+1
    i=1+1
print("The total number of times",char"has occurred=",count)


lower=int(input("Enter a lower range: "))
upper=int(input("Enter a upper range: "))
print("Prime numbers between",lower,"and",upper,"are: ")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%1)==0:
                break
        else:
            print(num)


def middle_product(n):
    s=str(abs(n))
    l=len(s)
    if l%2==0:
        return int(s[l//2-1])*int(s[l//2])
    else:
        return int(s[l//2])**2
print(middle_product(123456))
print(middle_product(12345))