# problem - 05
# Python program to remove an empty element from a list.

"""
Given
num = [“Hello”, 34, 45, ””, 40]
Expected output
Result : [‘Hello’, 34, 45, 40]
"""

# solution - 01

num = ["Hello", 34, 45, "", 40]
new_list = list(filter(None, num))

print("Result : ", new_list)
                
