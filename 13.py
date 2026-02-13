#write a python program to check leap year

year = int(input("Enter the year"))

#divided by 100 means century year(ending with 00)
#century year is divided by 400 is a leap year
if (year%400 == 0) and (year%100 == 0):
    print("{0} is a leap year".format(year))

#not divided by 100 means not a century year
# year divided by 4 ia a leap year 
elif (year % 4 ==0) and (year %100 !=0):
    print(f"{0} is a leap year ".format(year)) 

#if not divided by both 400(century year) and 4 (not century year)
#year is not leap year

else: 
    print(f"{0} is not a leap year".format(year))
