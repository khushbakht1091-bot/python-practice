# Problem: Read a, an operator (+ - * /) and b. Print the result.
# Handle division by zero and unknown operators with clear messages.

a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
op = input("Enter operator : ").strip()


if op == "+":
    print(a+b)

elif op == "-":
    print(a-b)

elif op == "*":
    print(a*b)

elif op == "/":
    if b == 0:
        print("Error: division by zero")
    else:
        print(f"{a/b:.2f}")

else:
    print("Invalid Operator")
