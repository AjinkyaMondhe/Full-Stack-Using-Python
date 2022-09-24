"""
8. Write a Python script to print distinct elements along with their frequencies of
occurrence in the list.
"""
list = [9,1,2,3,3,4,4,5,6,9]
for ele in set(list):
  print("Element: %d," %ele, "Frequency is: {}".format(list.count(ele)))