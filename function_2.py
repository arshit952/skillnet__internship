def greet(name):
    print(f"Hello {name}")
greet("Arshit")



def add(a,b):
    return a + b
r= add(2,5)
print(r )



def display(*args):
    print(args)
display("mango", "orange", "blueberry")




def student_info(name, age, rollnumber):
    print("Name:", name)
    print("Age:", age)
    print("Roll Number:", rollnumber)
student_info(name="Arshit", age=19, rollnumber=813)