# Problem: Find the second largest distinct value in a list without sorting.
# Sample: [4, 9, 2, 9, 7] → 7

x = [7, 9, 2, 9, 4]

largest = None
second_largest = None
# Use None to handle the negative values as well.

for num in x:
    if largest is None or num > largest:
        # Previous largest becomes second largest
        second_largest = largest
        largest = num

    # a != largest --> To handle duplicate values
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num


print("Second Largest : ", second_largest)
