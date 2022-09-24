#7. Write a Python script to remove all non int values from a list.

list = ["Ajinkya",1,2,3,4.5,-12.4,12,True,"A",-47]
list1=[]

for i in list:

  if  (type(i) == int):
      list1.append(i)
      
print(list1)