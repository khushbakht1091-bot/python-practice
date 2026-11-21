# Problem: Using a while loop, print the count of digits and the sum of digits of a number.


num = abs(int(input("Enter a number : ")))

count = 0
digit_sum = 0

if num == 0:
    count = 1

else:
    while num > 0:
        count += 1
        digit_sum += (num % 10)
        num //= 10


print(f"digit_sum : {digit_sum}")
print(f"Count : {count}")
