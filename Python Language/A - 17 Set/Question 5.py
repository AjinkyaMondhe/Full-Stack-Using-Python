"""
5. Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
"""

thisset = {"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}

unionset = thisset.union(secondset)
print(unionset)