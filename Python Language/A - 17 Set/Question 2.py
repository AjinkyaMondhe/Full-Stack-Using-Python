#2. Write a python program to store your own information {name, age, gender, so on..}


s = input("Enter Your Own Information: ")
Info = {eval(e) for e in s.split(',')}
print(Info)