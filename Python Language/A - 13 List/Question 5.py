"""
5. Write a python script to add an item to the end of the list (item “Python”. (mylist =
["Java", "SQL", "C", "Reactnative"]
"""
mylist = ["Java", "SQL", "C", "Reactnative"]
mylist.append("Pythonn")
print(mylist)
#------------Another Approach-------------

# if index > lastindex of list then automatically item will be inserted at last of list
mylist.insert(5,"Python")
print(mylist)