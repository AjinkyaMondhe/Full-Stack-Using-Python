"""
9. Write a Python script to create a list of city names taken from the user.
""" 


n = int(input("Enter Number of Cities: "))
city = []
i=0
print("Enter The Names of Cities")
while i<n:
  city.append(input())
  i+=1
print(city)