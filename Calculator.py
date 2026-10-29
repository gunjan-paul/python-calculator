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
opp = int(input("What would you like to do with these numbers:\n"
"1. Addition\n"
"2. Subtraction\n"
"3. Multiplication\n"
"4. Division\n"
"Just enter the number "))
while opp < 1 or opp > 4:
    opp = int(input("Must enter a number from the operations "))
if opp == 1:
    add(a,b)
elif opp == 2:
    order = int(input(f"1. {a}-{b} or 2. {b}-{a}? "))
    while order > 2 or order < 1:
            order = int(input("Enter a number from the order list "))
    if order == 1:
        sub(a,b)
    elif order == 2:
        sub(b,a)
elif opp == 3:
    mul(a,b)
elif opp == 4:
    order = int(input(f"1. {a}/{b} or 2. {b}/{a}? "))
    while order > 2 or order < 1:
            order = int(input("Enter a number from the order list "))
    if order == 1:
        div(a,b)
    elif order == 2:
        div (b,a)