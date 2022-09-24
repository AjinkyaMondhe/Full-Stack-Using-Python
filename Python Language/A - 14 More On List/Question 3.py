#3. Write a Python script to create a list of first N even natural numbers.

EvenNumber = []

i=2
N = int(input("Enter a Number for item in list: "))
while i<=2*N:
  EvenNumber.append(i)
  i+=2
print(EvenNumber)