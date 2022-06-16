# problem - 11
# Write a program in Python to choose a random item from a list.

"""
Given
num = [2,3,4,5,6,8,9]

Expected output
Result: 6
"""


import random
# solution - 01
num = [2,3,4,5,6,8,9]

ran = random.choice(num)
print(ran)
