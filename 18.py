#Write a python program to print a fibonacci series

nterms = int(input("How many terms?"))
n1,n2 = 0,1
count = 0

#first two terms
if nterms <= 0:
    print("Please enter a positive number")
#if there is only one term, return n1
elif nterms == 1:
    print(f"Fibonacci sequence upto", nterms, ":")
    print(n1)
else :
    print("Fibonacci Sequence")
    while count < nterms:
        print(n1)
        nth = n1 +n2
        #update values
        n1 = n2
        n2 = nth
        count += 1



