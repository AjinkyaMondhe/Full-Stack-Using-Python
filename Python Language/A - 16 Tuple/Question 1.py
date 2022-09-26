"""
1. Write a python script to store multiple items in a single variable ( Items are “Java”
,“Python”, “SQL”, “C” ) using tuple
"""
# 1'st Way
tup1 = ("Java","Python","SQL","C")
print(tup1)
print(type(tup1))

# 2'nd Way
tup2 = tuple(['Java','Python','SQL','C']) #Converting list into Tuple
print(tup2)
print(type(tup2))

# User Input in Tuple
tup = tuple([e for e in input().split(',')])
print(tup)