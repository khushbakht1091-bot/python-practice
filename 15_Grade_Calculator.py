# Problem: Convert marks (0–100) to a grade: A
# (90+), B (80–89), C (70–79), D (60–69), F (below 60).
# Anything outside 0–100 is Invalid marks.

marks = int(input("Enter marks : "))

if marks > 100 or marks < 0:
    print("Invalid marks")

elif marks >= 90:
    print("A")

elif marks >= 80:
    print("B")

elif marks >= 70:
    print("C")

elif marks >= 60:
    print("D")

else:
    print("F")
