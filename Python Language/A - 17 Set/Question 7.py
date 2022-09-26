'''
7. Write a python program to remove last item of the given set 
thisset = {"Python", "Django", "JavaScript", “SQL”}
'''

# Actually We Cannot Mention first item or last item in the set bcoz they are unordered/Unindexed So.

#This Program Choose Random Value/key and deletes it.
thisset = {"Python", "Django", "JavaScript","SQL"}
ans = thisset.pop()
print(ans)
print(thisset)

#If You Want To Remove Last Item Then Below is the Program
'''

thisset = {"Python","JavaScript","SQL","Django"}
thislist = list(thisset)
print("The Elements In List are:")
print(thislist)
print("Removed Element is: ",thislist.pop())
print(thislist)

'''