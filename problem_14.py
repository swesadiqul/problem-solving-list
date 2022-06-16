# problem - 14
# Write a program to enter or append n numbers in a list.

"""
Input: 2
Enter element at index 1: 2
Enter element at index 2: 4

Expected output
Result: [‘2’, ‘4’]
"""

# solution - 01
n = int(input("Enter any int number: "))
count = 1
list1 = []

for x in range(n):
    f = input(f'Enter element at index {count} : ')
    list1.append(f)
    count+=1

print("Result : ", list1)
    
