# problem - 07
# Write a program to display those items from a list that is divisible by 5.

"""
Given
num = [3, 5, 7, 9, 23, 15]
Expected output
Result: 5  15
"""

# solution - 01

num = [3, 5, 7, 9, 23, 15]
print("Result : ", end=" ")

for x in num:
    if (x%5==0):
        print(x, end=" ")
