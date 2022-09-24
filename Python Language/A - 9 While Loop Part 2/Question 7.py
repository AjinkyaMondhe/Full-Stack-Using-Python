#Write a python script to print first N even natural numbers in reverse order

n = int(input("Enter a Number: "))
i = 2*n
while (i>=1):
  print(i,end=" ")
  i-=2