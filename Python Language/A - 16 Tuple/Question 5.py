#5. Write a python program to check if all items in the tuple are the same.
tup1 = (10,20,30,40)
tup2 = (10,20,30,40)

i = 0
length = len(tup1)

if(len(tup1) != len(tup2)):
  print("Not Same (By Length)")
  exit()

while i<length:
  if tup1[i] == tup2[i]:
    pass
  else:
    print("Not Same (By Value)")
    break
  i+=1
else:
  print("All items are same")