import math 
from datetime import datetime
import calendar
def main():
    now=datetime.now()
    print("current date and time:",now)
    print("year:",now.year)
    print("month:",now.month)
    print("day:",now.day)
    print("hour:",now.hour)
    print("minute:",now.minute)
    print("second:",now.second)
    specific_date=datetime(2023,7,5,12,30,45)
    print("\n specific date and time:",specific_date)
    formatted_date=now.strftime("%y-%m-%d:%H:%M:%S")
    print("\n formatted date and time:",formatted_date)
    #calculate the difference between two dates
    date1=datetime(2023,7,1)
    date2=datetime(2024,7,1)
    difference=date2-date1
    print("\n Difference in days between 2023-07-01 and 2024-07-01:",difference.days)
    print("\n square root of 16:",math.sqrt(16))
    print("factorial of 5:",math.factorial(5))
    print("cosine of 0 radians:",math.cos(0))
    #math constants
    print("\n value of pi:",math.pi)
    print("value of e:",math.e)
    #Logarithms
    print("\n Natural Logarithm of 10:",math.log(10))
    print("Base-10 logarithm of 10:",math.log10(10))
    #Trigonometric functions
    angle=math.radians(45)#convert degrees to radians
    print("\n sine of 45 degrees:",math.sin(angle))
    print("cosine of 45 degrees:",math.cos(angle))
    print("Tangent of 45 degrees:",math.tan(angle))
    #Calendar functionalities
    year=now.year
    month=now.month
    #print the calendar for the current month
    print("\n calender for the current month:")
    print(calendar.month(year,month))
    #check if the current year is a leap year
    is_leap=calendar.isleap(year)
    print(f"Is(year)a leap year?:",is_leap)
    #print the number of leap years between two years
    start_year=2000
    end_year=2023
    leap_days=calendar.leapdays(start_year,end_year)
    print(f"Number of leap years between {start_year}and {end_year}:",leap_days)
if __name__=="__main__":
    main()




