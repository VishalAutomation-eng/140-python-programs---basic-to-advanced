#Write a python program to find Armstrong number in an interval

#input the interval from the user
lower = int(input("Enter the lower interval limit:"))
upper = int(input("Enter the upper interval limit:"))

for num in range(lower, upper+1):
    order = len(str(num))
    temp_num = num
    sum = 0

    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10
    # check if an num is an armstrong number 
    if num == sum:
        print(num)