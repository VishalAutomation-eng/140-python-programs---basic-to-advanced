#Write a python programs to check armtrong number

num = int(input("Enter the number"))

#calculate number of digits in num 
num_str = str(num)
num_digits = len(num_str)

#initialize variables
sum_of_powers = 0
temp_num = num

#calculate the sum of digits raised to the power of num_digits
while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit**num_digits
    temp_num //= 10

#check if it is an armstrong number

if sum_of_powers == num:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not armstrong number")

    