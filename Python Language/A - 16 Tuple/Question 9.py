"""
9. Write a python program to print the value 20 from given nested tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
"""
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

for itr in tuple1:
  for ele in itr:
    if ele == 20:
      print(20)
      exit() #If We Use break keyword here still else block will be executed
else:
  print("No Present")


'''
for itr in tuple1:
  i=0
  while i<len(itr):
    if itr[i] == 30:
      print("Yes")
      exit()
    i+=1
else:
  print("No")
'''