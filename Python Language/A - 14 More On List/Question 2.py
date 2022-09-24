#2. Write a Python script to create a list of first N odd natural numbers.

OddNumber = []
i=1
N = int(input("Enter a Number for item in list: "))
while i<=2*N:
  OddNumber.append(i)
  i+=2
print(OddNumber)