tree1=98
tree2=94
tree3=41
tree4=95
tree5=11

sum=tree1+tree2+tree3+tree4+tree5
print("The sum of all the 5 trees is: ",sum)
average=sum/5
print("The avreage of all the trees is: "average)


Amount=int(input("Please Enter Amount To Withdraw: "))
note1=Amount//100
note2=(Amount%100)//50
note3=((Amount%100)%50)//10

print("Notes of 100 rupees to be withdrawn: ",note1)
print("Notes of 50 rupees to be withdrawn: ",note2)
print("Notes of 10 rupees to be withdrawn: ",note3)


maths_score = 40
science_score = 50
hindi_score = 60
english_score = 70

total_score = maths_score + science_score + hindi_score + english_score

total_assumed_score=4*100

percentage = (total_score / total_assumed_score) * 100

print(f"Raj's percentage is: {percentage}%")


maths_score =int (input("Please enter your maths marks: "))
science_score = int (input("Please enter your science marks: "))
hindi_score =int ( input("Please enter your hindi marks: "))
english_score = int (input("Please enter your english marks: "))

total_score = maths_score + science_score + hindi_score + english_score

total_assumed_score=4*100

percentage = (total_score / total_assumed_score) * 100

print(f"Your percentage is: {percentage}%")