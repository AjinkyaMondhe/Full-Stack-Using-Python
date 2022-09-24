#5. Write a python script to calculate sum of first N even natural numbers

n = int(input("Enter a Number: "))
sum = 0

for i in range(0,2*n+1,2):
    sum +=i
print(sum)