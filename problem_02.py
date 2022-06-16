# problem - 02
# Write a program to count the number of items stored in a list.

"""
num = [23, 34, ‘hello’, 32, 56]
Expected output
Total count of items are: 5
"""


# solution - 01
num = [23, 34, "hello", 32, 56]
count = 0

for x in num:
    count +=1

print("Total count of items are: ", count)

# solution - 02

num = [23, 34, "hello", 32, 56]

count = len(num)
print("Total count of items are: ", count)
