# Reverse an integer using math (not string slicing) and say if it is a palindrome.

orignal_num = int(input("Enter a number : "))
num = abs(orignal_num)
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if orignal_num < 0:
    rev = -rev

print(f"Reversed : {rev}")

if orignal_num >= 0 and orignal_num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
