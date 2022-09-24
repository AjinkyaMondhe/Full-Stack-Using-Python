#4. Write a python script to calculate sum of first N odd natural numbers

num = int(input("Enter a Number: "))
sum = 0

for i in range(1,2*num+1,2):
    sum +=i
print(sum)