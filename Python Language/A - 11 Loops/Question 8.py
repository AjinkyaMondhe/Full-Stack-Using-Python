
#8. Write a python script to calculate sum of digits of a given number

num = int(input("Enter a Number: "))

sumDigit = 0

for i in range (num):
  if(num == 0):
    break
  dig = num % 10
  sumDigit +=  dig
  num //= 10
print(sumDigit)