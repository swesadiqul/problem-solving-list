# problem - 10
# Write a program in Python to remove duplicate items from a list.

"""
Given
num = [2,3,4,5,2,6,3,2]

Expected output
Result: [2, 3, 4, 5, 6]
"""


# solution - 01

num = [2,3,4,5,2,6,3,2]
x = []

for i in range(len(num)):
    if num[i] not in x:
        x.append(num[i])
    else:
        pass

print("Result : ", x)
    
