#8. Write a python script to check if a string contains only numbers.

#------------------------XXXXXXX---------------------------
# s1.isalpha = Check if string has Only alphabets no Numbers
# s1.isnumeric or s1.isdigit = Check if string has Only Numbers no alphabets
# s1.isalnum = Check if string is alpha-numeric(i.e: Both alphabets as well as numeric) if anyone is present then also True

string1 = "1a2b3c4d"
string2 = "1234"

print(string1.isdigit())
print(string2.isnumeric())
