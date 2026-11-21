# Problem: Print the sum of 1 to N using a loop, then verify it using the formula n(n+1)/2.

N = int(input("Enter : "))

if N < 0:
    print("Enter a non negative integer.")

else:
    sum = 0
    for x in range(1, N+1):
        sum += x

    formula = N*(N+1) // 2

    print("Loop Sum : ", sum)
    print("Formula Sum : ", formula)
