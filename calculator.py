def dummy():
    pass
    
def add():
    print("addition")
    a = int(input("enter the num1:"))
    b = int(input("enter the num2:"))
    print(a + b)

def sub():
    print("Subtraction")
    a = int(input("enter the num1:"))
    b = int(input("enter the num2:"))
    print(a - b)

def mul():
    print("multiplication")
    a = int(input("enter the num1:"))
    b = int(input("enter the num2:"))
    print(a * b)

def div():
    print("Division")
    a = int(input("enter the num1:"))
    b = int(input("enter the num2:"))
    print(a / b)

choice = True

while choice:
    ch = int(input("enter the choice:"))

    if ch == 1:
        add()
    elif ch == 2:
        sub()
    elif ch == 3:
        mul()
    elif ch == 4:
        div()
    else:
        print("invalid choice")
