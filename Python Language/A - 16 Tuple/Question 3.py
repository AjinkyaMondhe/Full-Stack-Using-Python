#3. Write a python program to reverse the tuple.

# 1st Way Using Slicing Operator
tup1 = (10,20,30,40,50)
print(tup1[::-1])

# 2nd Way Using Loop
i=len(tup1)-1
while i>=0:
  print(tup1[i],end=" ")
  i-=1

