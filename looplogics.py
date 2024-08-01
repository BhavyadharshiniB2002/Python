
#leap year
year=int(input("enter leap year:"))
if(year%400==0)and(year%100==0):
 print("{} is a leap year".format(year))
elif(year%4==0)and(year%100!=0):
   print("{} is a leap year".format(year))
else:
     print("{} is not a leap year".format(year))

#even or odd
num=int(input("enter your number:"))
if num%2==0:
  print("even number")
else:
  print("odd number")
