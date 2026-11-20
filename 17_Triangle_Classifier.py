# Problem: Given three sides, say whether it forms a valid triangle.
# If valid, print equilateral, isosceles or scalene, and also whether it is right-angled.


a = int(input("Enter first side : "))
b = int(input("Enter second side : "))
c = int(input("Enter third side : "))

# Validity Check
if a > 0 and b > 0 and c > 0 and (a+b > c) and (b+c > a) and (a+c > b):
        print("Valid")

        
        # Classification
        if a == b and b == c:
            print("Equilateral")

        elif a == b or b == c or c == a:
            print("Isosceles")

        else:
            print("Scalene")

        # Right Angle Check
        hyp = max(a,b,c)
        if (a**2 + b**2 + c**2) - hyp**2 == hyp**2:
            print("Right Angle Triangle")

else:
    print("Invalid")


