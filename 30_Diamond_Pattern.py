# Problem: Print a diamond of height 2n−1. Sample: 3 →
#    *
#   ***
#  *****
#   ***
#    *
n = int(input("Enter number : "))
if n < 0:
    print("Please enter a non-negative integer")

else:
    # Upper Half
    for i in range(1, n+1):
        space = " " * (n-i)
        stars = "*" * (2*i - 1)
        print(space + stars)
    # Lower Half
    for j in range(n-1, 0, -1):
        space = " " * (n-j)
        stars = "*" * (2*j - 1)
        print(space + stars)
