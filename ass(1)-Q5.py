a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a < b and a < c:
    print(a,"is the smallest no")
elif b < a and b < c:
    print(b,"is the smallest no")
else:
    print(c,"is the smallest no")