#1. Write a Python script to create a list of first N natural numbers.

NaturalNumber = []

i=1
N = int(input("Enter a Number for item in list: "))
while i<=N:
  NaturalNumber.append(i)
  i+=1
print(NaturalNumber)