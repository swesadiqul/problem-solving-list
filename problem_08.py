# problem - 08
# Write a program to sum all the elements of a list.

"""
Given
num = [2,3,2,4,7,8]

Expected output
Sum of list items 26
"""


# solution - 01
num = [2,3,2,4,7,8]

sum1 = 0

for x in num:
    sum1 = sum1 + x

print("Sum of list items : ", sum1)
