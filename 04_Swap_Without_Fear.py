# Problem:
# Swap the values of two variables in three ways:
# with a temporary variable, with tuple unpacking, and with arithmetic only.

# Temporary variable
print("--Temporary variable--")
a = 3
b = 9

print("a : ", a)
print("b : ", b)
c = a
a = b
b = c
print("a : ", a)
print("b : ", b)

# Tuple unpacking
print("--Tuple unpacking--")
x, y = (3, 9)
print("x : ", x)
print("y : ", y)
y, x = x, y
print("x : ", x)
print("y : ", y)

# Arithmetic
print("--Arithmetic--")
num1 = 3
num2 = 9

print("num1 : ", num1)
print("num2 : ", num2)

num1=num1+num2
num2=num1-num2 
num1=num1-num2

print("num1 : ", num1)
print("num2 : ", num2)

