"""
9. Write a python script to print binary equivalent of a given decimal number.
(do not use bin() method)
"""

num = int(input("Enter a Decimal Number: "))
l =[]
while num!=0:
  r= num%2
  l.append(r)
  num//=2
l.reverse()

for ele in l:
  print(ele,end="")