# Problem: Print the table of a given number up to 10, formatted neatly.
# Sample: 5 → 5 x 1 = 5 … 5 x 10 = 50


n = int(input("Enter a number : "))
start = int(input("Enter the start of the table : "))
end = int(input("Enter the end of the table : "))

if start > end:
    print("Start should not be greater than end.")
else:
    for x in range(start, end+1):
        print(f"{n} x {x} = {n*x}")
