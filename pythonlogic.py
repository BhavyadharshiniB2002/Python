
#palindrom
'''a=int(input("enter the number:"))
b=a
c=0
while (b>0):
    r=b%10
    c=(c*10)+r
    b=b//10
print(c)
if a==c:
    print("it is not a palindrome")
else:
    print("it is not")'''

#string palindrom
'''a=input("enter the name:")
b=a[::-1]
if a==b:
    print("it is a palindrome")
else:
    print("it is not a palindrome")'''

#adam no
'''num=int(input("enter the number:"))
a=num
b=a*(a)
c=0
while(b>0):
    r=b%10
    c=(c*10)+r   
    b=b//10
print(c)
print(b)
if c==b:
    print("it is adam number")
else:
    print("it is not adam number")'''

#adam number
'''number=int(input("enter the first value:"))
s1=number
squr=s1*s1
value1=0
while(squr>0):
    r=squr%10
    value1=(value1*10)+r
    squr=squr//10
print(value1)
temp=0
while(s1>0):
    r=s1%10
    temp=(temp*10)+r
    s1=s1//10
print(temp)
value2=temp*temp
print(value2)
if (value1==value2):
    print("adam number")
else:
    print("not adam number")'''

#amstrong number
'''a=int(input("enter the number:"))
num=a
b=num*num*num
print(b)
c=int(input("enter the number"))
num=c
d=0
while(num>0):
    r=num%10
    d=d+(r**3)
    num=num//10
print(d)
if d==c:
    print("amstrong number")
else:
    print("not aamstrong number")'''

#file handling adam no
'''from kk import  *
a=int(input("enter the value:"))
if reverse(val(a))==val(reverse(a)):
    print("it is adam no")
else:
    print("not adam no")'''


# #fibonacci series
'''num=int(input("enter the value:"))
a=0
b=1
for i in range(num):
    a=(a)
    c=(a)
    a=b
    b=c+b
print(b)
a=int(input("enter the value:"))
f1,f2=0,1 
f3=f1+f2
print("fibonacci no",a)
print(f1)
print(f2)
for i in range(5):
    print(f3)
    f1=f2
    f2=f3
    f3=f1+f2'''


# #factorial
'''sum=int(input("enter the number"))
def fact(sum):
    fact=1
    sum=int(input("enter the number"))
    for i in range(1,sum+1):
      fact=fact*i
    return fact
print("factorial value",fact(sum))'''

#fact 2nd method
'''num=int(input("enter a number:"))
fact=1
if num<0:
    print("factorial does not exist for negative")
elif num==0:
    print("the factorial of o is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
        print("the facorial of",num,fact)'''

#python logic with function
'''def pali(c):
    a=int(input("enter the value:"))
    b=a*a
    while(b>0):
        r=b%10
        c=(c*10)+r
        b=b//1
        print(c)
        print(b)
    if c==b:
        print("it is adam number")
    else:
        print("it is not adam number")
def amstrong(b):
    num=a
    b=num*num*num
    print(b)
    num=c
    d=0
    while(num>0):
        r=num%10
        d=d+(r**3)
        num=num//10
        print(d)
    if d==c:
        print("amstrong number")
    else:
        print("not aamstrong number")
        num=int(input("enter the number:"))
def adam():
    a=num
    b=a*(a)
    c=0
    while(b>0):
        r=b%10
        c=(c*10)+r   
        b=b//10
        print(c)
        print(b)
        if c==b:
            print("it is adam number")
        else:
            print("it is not adam number")
def palindrome(c):
    b=a
    c=0
    while (b>0):
        r=b%10
        c=(c*10)+r
        b=b//10
        print(c)
    if a==c:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
def fibonacci(c):
    f1,f2=0,1 
    f3=f1+f2
    print("fibonacci no",a)
    print(f1)
    print(f2)
    for i in range(5):
        print(f3)
        f1=f2
        f2=f3
        f3=f1+f2
def fact(c):
    for i in range(1):
      fact=fact*i
    return fact
print("factorial value",fact(c))
def palin(c):
    b=a[::-1]
    if a==b:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
n=int(input("enter your choice1.adam\n2.amstrong\n,3.palindrome\n4.fibonacci\n5.factorial\n6.palin"))
c=int(input("enter your number"))
if n==1:
    adam(c)
elif n==2:
    amstrong(c)
elif n==3:
    palindrome(c)
elif n==4:
    fibonacci(c)
elif n==5:
    fact(c)
elif n==6:
    palin(c)
else:
    print("please enter the correct input")'''

#fuction
'''def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def mod(a,b):
    print(a%b)
c=1
while(c==1):
    n=int(input("enter your choice1.add\n2.sub\n3.mul\n4.div\n5.mod"))
    a=int(input("enter the first value:"))
    b=int(input("enter the second value:"))
    if (n==1):
        add(a,b)
    elif (n==2):
        sub(a,b)
    elif (n==3):
        mul(a,b)
    elif (n==4):
        div(a,b)
    elif (n==5):
        mod(a,b)
    else:
        print("enter correct value")
        c=int(input("if you want continue,please enter 1?"))'''
    

#prime or not
'''n=int(input("enter your value:"))
count=0
for i in range(1,n):
    if n%i==0:
        count=count+1
if count==1:
    print("prime")
else:
    print("not")'''

#even or odd
'''string=input("enter the string")
number=string[2]
if (number=="a"):
    a=int(input("enter the value"))
    if a%2==0:
        print("even number")
    else:
        print("odd number")'''