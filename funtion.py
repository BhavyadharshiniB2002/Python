
#function
#basic
def myfunction():
   print("hello world")
myfunction()

#argument
def addnum(num1,num2):
   print(num1+num2)
addnum(2,3)

#return keyword
def function(name,age):
   print(name,age)
function("livewire",23)
def multiplynum(num1):
 return num1*7
result=multiplynum(8)
print(result)

#recursion
def factorial(x): 
   if x==1:
    return 1
   else:
    return (x*factorial(x-1))
num=5
print("the factorial of",num,"is",factorial(num))

#arbitrary(*,**)
def myfunction(*kids):
  print(kids[0])
myfunction("emil","bijorn","linus")
def my_function(**kid):
  print("his last name is"+kid["fname"]+kid["lname"])
my_function(fname="harish",lname="bijorn")

#workout
def my_function(country="norway"):
  print("I am from"+country)
my_function("sweden")
my_function()
my_function("india")

#lambda function
gift=lambda person:print("bhavya",person)
gift("watch")

#workout
x=lambda a,b:a*b
print(x(4,7))
def myfun(n):
  return lambda a:a*n
m=myfun(2)
print(m(11))
print(m(45))

#filering,mapping
data=[1,2,3,4,5,6,7,8,9]
result1=map(lambda x:x*2,data)
print(list(result1))
print(result1)
result2=filter(lambda x:x%2==0,data)
print(list(result2))
print(result2)



