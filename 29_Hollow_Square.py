# Problem: Print a hollow square of size n made of *. Sample: 4 →
# ****
# *  *
# *  *
# ****

n = int(input("Enter a number : "))

if n < 0:
    print("Enter a non-negative integer")
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end="")
            else:
                print(" ", end="")

        print()
