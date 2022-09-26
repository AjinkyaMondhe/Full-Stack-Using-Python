"""
10. Write a python program to change the first item (22) of a list within the following tuple
to 222. tuple1 = (11, [22, 33], 44, 55)
"""
tuple = (11, [22, 33], 44, 55)
list1 = list(tuple)
list1.remove([22,33])
list1.insert(1,[222,33])
print(list1)

"""
list1 = list(tuple)
print(list1)
for ele in list1:
  if ele == 11:
    idx = list1.index(ele)
    list1[idx] = 111
print(list1)
"""