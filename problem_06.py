# problem - 06
# Python program to append an element to a list.

"""
Given
num = [23,45,67,8,9]
Input:
Enter the item to insert: study

Expected output
Result: [23,45,67,8,9, ‘study’]
"""


# solution - 01
num = [23,45,67,8,9]

user_input = input('Enter the item to insert: ')
num.append(user_input)
print("Result : ", num)
