#write a python program to find a factorial of a number.

num = int(input("Enter the number for calculating a factorial"))

factorial = 1
if num <0:
    print("Factorial does not exist for negative numbers")
elif num ==0:
    print("factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print(f"The factorial of {num} is {factorial}")