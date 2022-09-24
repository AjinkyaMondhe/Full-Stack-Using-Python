'''
Write a python script to display the current date and time. First create
variable to store date and time, then display date and time in proper format 
(line: 13-8-2022 and 9:00 PM)
'''

from datetime import datetime
dt = datetime.today()
print(dt)
d1 = dt.strftime("%d-%m-%Y and %I:%M:%S %p")
print(d1)
'''
d1 = dt.strftime("%d-%b-%y")
print(d1)
#24 Hours Format
d1 = dt.strftime("%H:%M:%S %p")
print(d1)
#12 Hours Format
d1 = dt.strftime("%I:%M:%S %p")
print(d1)
# B means August and b means Aug
d1 = dt.strftime("%d-%B-%Y")
print(d1)
d1 = dt.strftime("%d-%b-%Y")
print(d1)
'''