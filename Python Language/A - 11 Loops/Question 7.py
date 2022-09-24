#7. Write a python script to count digits in a given number

num = int(input("Enter a Number: "))
count = 0

for i in str(num):
  count +=1
print(count)