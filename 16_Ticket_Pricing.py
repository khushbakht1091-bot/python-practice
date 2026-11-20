# Problem: Ticket price by age:
# under 3 free, 3–12 (200), 13–59 (500), 60+ (300).
# If the visit is on a weekend (user answers yes/no), add 10%.

age = int(input("Enter age : "))
if age < 0:
    print("Invalid age")


else:
    on_weekend = input("If the visit is on a weekend (yes/no) : ")

    if age < 3:
        price = 0

    elif age <= 12:
        price = 200

    elif age <= 59:
        price = 500

    else:
        price = 300

    if on_weekend.lower().strip() == "yes":
        increase = 10
        price = price * (1 + increase/100)

    print(int(price))
