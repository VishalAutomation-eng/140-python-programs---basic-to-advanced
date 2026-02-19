#write a python program for cube sum of first n natural numbers

def cube_sum_of_natural_numbers(n):
    if n<=0:
        return 0
    else:
        total = sum([i**3 for i in range(1, n+1)])
        return total


n = int(input("Enter the value of n:"))

if n <= 0:
     print("Please enter a positicve number")
else:
    result = cube_sum_of_natural_numbers(n)
    print(f"The cude sum of the first {n} natural number is : {result}")

