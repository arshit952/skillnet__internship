
print("select the opertion")
print("1.for Addition")
print("2.for Subtraction")
print("3.for Multipy")
print("4.for Divide")
print("5.for Modulus")
operator=int(input("Select opertion from 1 to 5-->"))
num1=int(input("enter the number-->"))
num2=int(input("Enter the number-->"))
if(operator==1):
    {
        print("Sum of two numbers is-->",num1+num2)
    }
elif(operator==2):
    {
        print("subtract is-->",num1-num2)
    }
elif(operator==3):
    {
        print("multiply is-->",num1*num2)
    }
elif(operator==4):
    {
        print("Divide is-->",num1/num2)
    }
elif(operator==5):
    {
        print("modulus is-->",num1%num2)
    }
else:
    {
        print("invaild input")
    }

