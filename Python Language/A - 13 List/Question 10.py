"""
10. Write a Python script to create a list, where each element of the list is a digit of a
given number.
"""

list = list(input("Enter a Number: "))
new_list =[]

for ele in list:
  new_list.append(int(ele))

print(new_list)