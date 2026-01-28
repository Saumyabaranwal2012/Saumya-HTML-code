medical=input("Please Enter YES or NO for medical cause: ")
attendence=int(input("Please enter your attendance record[no. of days you were present]: "))
if medical=="Yes":
    print("You are eligible to give your exams")
else:
    if attendence>=75:
        print("You are eligible to give your exams")
    else:
        print("You are not eligible to give your exams")


print("Select your ride:")
print("1. Bike/Scooter")
print("2. Car")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("What type of bike?")
    print("1. Scooty")
    print("2. Bike")

    choice2 = int(input("Enter your choice of type: "))
    if choice2 == 1:
        print("You have selected Scooty")
    elif choice2 == 2:
        print("You have selected Bike")
    else:
        print("Invalid choice")

elif choice == 2:
    print("What type of car?")
    print("1. Small")
    print("2. Big")

    choice2 = int(input("Enter your choice of type: "))
    if choice2 == 1:
        print("You have selected Small car")
    elif choice2 == 2:
        print("You have selected Big car")
    else:
        print("Invalid choice")

else:
    print("Invalid choice")
