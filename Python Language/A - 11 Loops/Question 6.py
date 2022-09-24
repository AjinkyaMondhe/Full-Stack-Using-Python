#6. Write a python script to calculate factorial of a given number
num = int (input("Enter a Number: "))
fact = 1

for i in range(1,num+1):
  fact = fact * i
print(fact)