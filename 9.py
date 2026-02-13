#Write a python program to solve a quadratic equation
"""
The standard form of a quadratic equation is:
                                            ax^2+bx+c = 0

                                            where, a,b and c are real numbers
                                            a != 0
The solution of quadratic equation is given by:
                                ----- see in code -----
"""

import math

#input coefficients
a = float(input("Enter the coefficient a:"))
b = float(input("Enter the coefficient b:"))
c = float(input("Enter the coefficient c:"))

#calculate the Decscriminant
discriminant = b**2 - 4*a*c

#check if the descriminant is positive , negative or zero
if discriminant > 0:
    #Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}") 
    print(f"Root 2: {root2}")

elif discriminant == 0:
    #one real root repeated
    root = -b / (2*a)
    print(f"Root:{root}")

else:
    #Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")