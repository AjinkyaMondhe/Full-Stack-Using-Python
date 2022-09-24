"""
Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part
"""

x = complex(input("Enter a number in complex format like 3+5j: "))
print( (x.real) if (x.real > x.imag)  else(x.imag))