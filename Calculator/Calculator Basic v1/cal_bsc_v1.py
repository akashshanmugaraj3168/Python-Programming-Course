print("Welcome to the Basic Calculator App! \nThis application was created by Akash Shanmugaraj")
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    op = input("Enter Operand [+ or - or * or /] ")
    if op == "+":
        print("The Result is "+str(num1+num2))
    elif  op == "-":
        print("The Result is "+str(num1-num2))
    elif  op == "*":
        print("The Result is "+str(num1*num2))
    elif  op == "/":
        print("The Result is "+str(num1/num2))

calculator()

val = "123"
while val == "123":
    calculator()
