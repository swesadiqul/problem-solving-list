# problem - 04
# Python program to square each element of a list.

"""
Given
x = [2, 3, 4, 5, 6]
Expected output
Result : 4 9 16 25 36
"""

# solution - 01

x = [2, 3, 4, 5, 6]
print("Result : ", end=" ")
for i in x:
    square = i * i
    print(square, end=" ")
