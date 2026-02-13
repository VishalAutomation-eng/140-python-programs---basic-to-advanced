#write a python program to display a calender
import calendar

year = int(input("Enter the year"))
month = int(input("Enter the month"))

cal = calendar.month(year,month)
print(cal)