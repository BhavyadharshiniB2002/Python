#if statement
name=input("enter your name:")
age=input("enter your age:")
city=input("enter your city:")
std=int(input("enter your std:"))
school=input("enter your school:")
tamil=int(input("enter your tamil marks:"))
english=int(input("enter your english marks:"))
maths=int(input("enter your maths marks:"))
total=tamil+english+maths
average=total/3
print(total)
print(average)
if total>250:
    print("you got a bio")
else:
    print("you got a com")

#if statement
num=int(input("Enter your number: "))
if num > 0:
   print("The number is positive")
else:
    print("negative number")

# if else
age=int(input("enter your age:"))
if age<18:
    print("your are eligible to vote")
else:
    print("your are not eligible to vote")
    
#if else
age=int(input("enter your age:"))
if age>25:
    print("your are eligible to election:")
else:
    print("your are  not eligible to election:")

#workout
student=int(input("enter your number:"))
name=str(input("enter your name:"))
std=int(input("enter your std:"))
age=int(input("enter your age:"))
place=str(input("enter your place:"))
tamil=int(input("enter your tamil marks:"))
english=int(input("enter your english marks:"))
maths=int(input("enter your maths marks:"))
science=int(input("enter your science marks:"))
social=int(input("enter your social marks:"))
total=tamil+english+maths+science+social
print(total)
if (total>400)and(age>=15):
    print("the student is bio")
    print("there is a markstatement")
else:
    print("the student is com")
    print("there is not markstatement")

    #elif
num=int(input("enter your number:"))
if num>30:
     print("good")
elif num==30:
    print("this is equal")
else:
    print("bad")

#nestedif
num=int(input("enter your number:"))
if num>=0:
 if num==0:
        print("this is equal to 0")
 else:
    print("this is positive number")
else:
    print("this is negative number")

#if workout
age=int(input("enter your age:"))
if(age<30):
    print("you are eligible")
else:
    print("you are not eligible")

    #nested
username=input("enter your username:")
password=input("enter your password:")
if username=="bhavya":
  if password=="livewire":
    print("login a successful!welcome admin")
  elif password=="12345":
    print("weak password.please reset your password")
  else:
    print("incorrect password.please try again")
else:
        if username=="dd":
           if password=="jan":
             print("login successful welcome dd")
           else:
             print("incorrect password please try again")
        else:
               print("unknown user.please try again")
