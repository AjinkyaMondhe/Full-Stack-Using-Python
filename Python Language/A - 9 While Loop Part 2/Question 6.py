#Write a python script to print first N even natural numbers

n = int(input("Enter a Number: "))
i = 1
while (i<=2*n):
  if(i%2==0):
    print(i,end=" ")
  i+=1