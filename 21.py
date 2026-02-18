#Write a python program to find sum of natural numbers

limit = int (input("Enter the limit:"))

#initialize the sum 
sum = 0

#use a for loop to calculate sum of natural numbers 
for i in range(1,limit+1):
    sum = sum + i

#print the sum 
print("The sum of natural numbers up to ", limit, "is:", sum)
