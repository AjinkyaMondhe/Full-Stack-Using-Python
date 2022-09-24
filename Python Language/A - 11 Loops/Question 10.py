"""
10. Write a python script to print the octal equivalent of a given decimal number. 
(do not use oct() method)
"""

num = int(input("Enter a Decimal Number: "))
l =[]
while num!=0:
  r = num % 8
  l.append(r)
  num //= 8
l.reverse()

for ele in l:
  print(ele ,end = " ")