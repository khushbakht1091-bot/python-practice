# Problem: Print a right-angled triangle of * with n rows.

n = int(input("Enter number of rows : "))

if n < 0:
    print("Please enter a non-negative integer")
else:
    for i in range(1, n+1):
        print("*" * i)
