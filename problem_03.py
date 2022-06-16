# problem - 03
# Write a program to reverse a list in Python.

"""
num = [23, 34, ‘hello’, 32, 56]
Expected output
[56, 32, ‘hello’, 34, 23]
"""


# solution - 01

num = [23, 34, "hello", 32, 56]
num.reverse()

print(num)


# solution - 02
num = [23, 34, "hello", 32, 56]
new_list = []

for x in num[::-1]:
    new_list.append(x)

print(new_list)

