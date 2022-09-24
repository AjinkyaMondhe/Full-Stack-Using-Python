"""
9. Write a Python script to print indices of all occurrences of a given element in a given
list.
"""

list  = [1,2,3,4,4,5,5,6,6,1,2,3,9,8,7]
for ele in list:
  print(ele,"Index are:-",list.index(ele))