# def adam(num):
#     value=0
#     while(num>0):
#         r=num%10
#         value=(value*10)+r
#         num=num//10
        
    
# def val(a):
#     return a*a

# python patterns
'''n=int(input("enter the number:"))
for i in range(n):
    for j in range(i+1):
        if j==0 or i==j or i==n-1:
            print("*",end=" ")
        else:
            print("",end=" ")
    print("")'''

#workout
'''value="bhavyadharshini"
for x in range(16):
   print(value[:x])
for x in range(6):
    print()
    for j in range(x):
        print(j,end="")'''

#patten2
#method1
'''num=int(input("enter number:"))
for i in range(num):
    for j in range(num):
        print("*",end="")
    print("")'''

#pattern3
#method1
'''for i in range(num):
    print("*"*num)'''

#pattern4
'''n=int(input("enter no:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")'''

#pattern5
#method1
'''n=int(input("enter number:"))
for i in range(0,n):
    for j in range(i+1):
        print("*",end="")
    print("")'''

#method2
'''for i in range(1,n+1):
    print("*"*i)
n=int(input("enter number:"))
for i in range(n,0-1):
    for j in range(i):
        print("*",end="")
    print()'''

#Student mark list
'''file=open("studentdetails.txt","w")
file.write("personal details:\n")
name=input("enter your name:")
age=int(input("enter your age:"))
if age>=18:
    print("your are eligible to college")
else:
    print("you are not")
course=input("enter your course:")
phoneno=int(input("enter your phoneno:"))
emailaddress=(input("enter your email address:"))
file.write("mark details:")
m1=int(input("enter your m1:"))
if m1>=35:
    print("pass")
else:
    print("fail")
m2=int(input("enter your m2:"))
if m2>=35:
    print("pass")
else:
    print("fail")
m3=int(input("enter your m3:"))
if m3>=35:
    print("pass")
else:
    print("fail")
m4=int(input("enter your m4:"))
if m4>=35:
    print("pass")
else:
    print("fail")
m5=int(input("enter your m5:"))
if m5>=35:
    print("pass")
else:
    print("fail")
total=m1+m2+m3+m4+m5
average=total/5
print(total)
print(average)
file.write(name)
file.write("\t")
file.write (str(age))
file.write("\t")
file.write(course)
file.write("\t")
file.write (str(phoneno))
file.write("\t")
file.write(emailaddress)
file.write("\t")
file.write(str(m1))
file.write("\t")
file.write(str(m2))
file.write("\t")
file.write(str(m3))
file.write("\t")
file.write(str(m4))
file.write("\t")
file.write(str(m5))
file.write("\t")
file.write(str(total))
file.write("\t")
file.write(str(average))
file.write("\t")
with open("studentdetails.txt") as f1:
    data=f1.read()
print(data)
file.close()'''

#workout
'''a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if (a%2!=0)and(b%2!=0)and(c%2==0):
    print(a+b+c)
elif(a%2!=0)and(b%2==0)and(c%2==0):
    print(a-b-c)
elif(a%2==0)and(b%2==0)and(c%2==0):
    print(a*b*c)
elif(a%2!=0)and(b%2!=0)and(c%2!=0):
    print(a/b/c)
else:
    print("does not correct value")
def check(i):
    if i%2==0:
        return 1
    else:
        return 0
a=int(input("enter your value:"))
b=int(input("enter your value"))
c=int(input("enter your value"))
i=check(a)+check(b)+check(c)
if i==0:
    print(a+b+c)
elif i==1:
    print(a-b-c)
elif i==2:
    print(a*b*c)
elif i==3:
    print(a/b/c)
else:
    print()'''

#random number
'''import random
a=random.randint(0,100)
while True:
    value=int(input("enter your value"))
    if a==value:
        print("correct answer")
        break
    elif a<value:
        print("less than")
    elif a>value:
        print("greater than")
    else:
        print("does not correct value")'''

#calender
'''import calendar
yy=int(input("enter your year"))
mm=int(input("enter your month"))
print(calendar.month(yy,mm))
value=[1,3,5,7,8,7,5,9]
a=value.sort()
a=value[0]
print(a)
def value(a,b):
    print(a+b,"the value")
value(2,3)'''

#function

'''def value(*num):
    value=0
    for i in num:
        value+=num
        return value
value()'''


    








    