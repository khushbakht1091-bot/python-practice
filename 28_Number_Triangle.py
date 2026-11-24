# Problem: Print the number triangle where row i contains the numbers 1 to i. Sample: 4 →
# 1
# 12
# 123
# 1234

n = int(input("Enter number : "))

if n < 0:
    print("Enter a non-negative integer")

else:
    for i in range(1, n+1):
        for j in range(1, i + 1):
            print(j, end="")

        print()
