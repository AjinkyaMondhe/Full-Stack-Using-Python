#4. Write a python program to Swap two tuples in Python.

tup1 = (10,20,30)
tup2 = (40,50,60)
print("Before Swapping")
print(tup1,tup2)
(tup1,tup2) = (tup2,tup1) # Swapping of Two Tuple.
print("After Swapping")
print(tup1,tup2)

#---- Another Way is Using Temp Vairable ----
'''
print(tup1,tup2)
temp = tup1
tup1 = tup2
tup2 = temp
print(tup1,tup2)

'''