#Write a python program to swap the two variables

#input two variables 

a = int(input("Enter the value of the first variable(a):"))
b = int(input("Enter the value of variable(b):"))

#display the original values
print(f"Entered value of variables: {a}, {b}")

temp = a
a = b
b = temp

#display the swapped values 
print(f"swapped values: a={a}, b = {b}")
