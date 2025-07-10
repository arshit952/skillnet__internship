def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def divide(x,y):
    return x/y
def average(x,y):
    return (x+y)/2
print("select the opertion")
print("1.for Addition")
print("2.for Subtraction")
print("3.for Multipy")
print("4.for Divide")
print("5.for Average")
operator=int(input("Select opertion from 1 to 5-->"))
num1=int(input("enter the number-->"))
num2=int(input("Enter the number-->"))
if(operator==1):
    {
        print("Sum of two numbers is-->",add(num1,num2))
    }
elif(operator==2):
    {
        print("subtract is-->",sub(num1,num2))
    }
elif(operator==3):
    {
        print("multiply is-->",multi(num1,num2))
    }
elif(operator==4):
    {
        print("Divide is-->",divide(num1,num2))
    }
elif(operator==5):
    {
        print("average is-->",average(num1,num2))
    }
else:
    {
        print("invaild input")
    }

