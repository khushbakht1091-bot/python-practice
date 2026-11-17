# Problem: This program should print the age next year. Find every error and fix it.
# Sample: Input: 20 → Output: Next year you will be 21 years old 

# age = input("Age: ")
# print("Next year you will be " + age + 1 + " years old")

# input() returns str

# Age: 20
# Traceback (most recent call last):
#    print("Next year you will be " + age + 1 + " years old")
#          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
# TypeError: can only concatenate str (not "int") to str



age = int(input("Age: "))
print(f"Next year you will be {age + 1} years old")
