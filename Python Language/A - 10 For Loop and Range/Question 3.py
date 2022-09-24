#3. Write a python script to print first N natural numbers in reverse order

n = int(input("Enter a number: "))
for i in range(n,0,-1):
  print (i,end=" ")
print()
for i in range(1,n+1):
  print (n,end=" ")
  n-=1