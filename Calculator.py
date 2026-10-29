def add(a,b):
    ans = a + b
    print(ans)
def sub(a,b):
    ans = a - b
    print(ans)
def mul(a,b):
    ans = a * b
    print(ans)
def div(a,b):
    if b == 0:
        print("Error: Cannot divide by zero.")
    else:
        ans = a/b
        print(ans)
while True:
    try:
        a = float(input("Enter your first number "))
        break
    except ValueError:
        print("Must enter a number ")
while True:
    try:
        b = float(input("Enter your second number "))
        break
    except ValueError:
        print("Must enter a number ")
while True:
    try:
        op = int(input("What would you like to do with these numbers:\n"
                        "1. Addition\n"
                        "2. Subtraction\n"
                        "3. Multiplication\n"
                        "4. Division\n"
                        "Just enter the number "))
        while op < 1 or op > 4:
            op = int(input("Must enter a number from the operations "))
        break
    except ValueError: 
        print("Must enter a number from the operations ")
if op == 1:
    add(a,b)
elif op == 2:
    while True:
        try:
            order = int(input(f"1. {a}-{b} or 2. {b}-{a}? "))
            while order < 1 or order > 2:
                order = int(input("Enter a number from the order list "))
            if order == 1:
                sub(a,b)
            elif order == 2:
                sub(b,a)
            break
        except ValueError:
            print("Enter a number from the order list ")
elif op == 3:
    mul(a,b)
elif op == 4:
    while True:
            try:
                order = int(input(f"1. {a}/{b} or 2. {b}/{a}? "))
                while order < 1 or order > 2:
                    order = int(input("Enter a number from the order list "))
                if order == 1:
                        div(a,b)
                elif order == 2:
                        div(b,a)
                break
            except ValueError:
                print("Enter a number from the order list ")