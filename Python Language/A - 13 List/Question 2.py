#2. Write a python script to get the data type of a list.


Homogeneous = ["Java","Python","SQL","C"]
for ele in Homogeneous:
  print(type(ele))
print("\n",type(Homogeneous))

Heterogeneous = ["A",True,3.5,10,3+5j]
for ele in Heterogeneous:
  print(type(ele))
print("\n",type(Heterogeneous))