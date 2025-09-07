num1 = float(input("Enter the first operand: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second operand: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2!= 0:
        result = num1 / num2
    else:
        print("Error: Division by zero!")
        result = None
elif operator == "^":
    result = num1 ** num2
elif operator == "#":
    result = num1 ** (1/num2)
else:
    print("Error: Invalid operator!")
    result = None

if result is not None:
    print("The result is:", result)