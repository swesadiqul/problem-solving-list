# problem - 12
# Write a program to append data of the second list to the first list.

"""
Given
list1 = [23, 24, 25, 26] list2 = [27, 28, 29, 30]

Expected output
Result: [23, 24, 25, 26, 27, 28, 29, 30]
"""


# solution - 01
list1 = [23, 24, 25, 26]
list2 = [27, 28, 29, 30]

list1.extend(list2)
print(list1)


# solution - 02
list1 = [23, 24, 25, 26]
list2 = [27, 28, 29, 30]

for x in list2:
    list1.append(x)

print(list1)
