# Problem: Print a centered pyramid with n rows. Sample: 3 →
#   *
#  ***
# *****

n = int(input("Enter number : "))

if n < 0:
    print("Please enter a non-negative integer")

else:
    for i in range(1, n+1):
        spaces = " " * (n-i)
        star = "*" * (2*i - 1)
        print(spaces + star)
