# problem - 13
# Write a program in Python to filter odd and even number from a list.

"""
Given
num = [2, 23, 24, 51, 46, 67]

Expected output
Even [2, 24, 46] Odd [23, 51, 67]
"""

# solution - 01
num = [2, 23, 24, 51, 46, 67]
x = []
y = []

for i in range(len(num)):
    if num[i]%2==0:
        x.append(num[i])
    else:
        y.append(num[i])

print("Enen : ", x, "Odd : ", y)
