# Build a calculator that asks the user for two numbers and an operation (like addition, subtraction, multiplication, or division), then prints the result.

# variable needed 2
# If Statement using str data type

print("Welcome to my First Calculator ")

print("Enter 2 Number: ") 
number1 = int(input("First Number: "))
number2 = int(input("Second Number: "))

print("Choose An operation + - * / ")

opr = str(input())

if (opr == "+"):
    print(number1 + number2)

if (opr == "-"):
    print(number1 - number2)
    
if (opr == "*"):
    print(number1 * number2)

if (opr == "/"):
    print(number1 / number2)

