# Problem: Read three numbers and print the largest without max().

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if b >= c:
    if a > b:
        print(f"Largest : {a}")

    else:
        print(f"Largest : {b}")

else:
    if c > a:
        print(f"Largest : {c}")

    else:
        print(f"Largest : {a}")


