age=int(input("Enter the age"))
gender=int(input("""Select the gender
                1>male
                 2>female """))
if(gender==1):
    print("Your male")
    if(age>=18):
        print("You can apply for liecence.male")
    else:
        print("You can't apply for liecence.")
elif(gender==2):
    print("your female")
    if(age>=21):
        print("Your are eligible for marriage")
    else:
        print("Your are noteligible for marriage")
