# Problem: Compute n! with a loop. Print a message for negative input.

n = int(input("Enter number : "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1
    for x in range(n, 1, -1):
        factorial *= x

    print(factorial)
