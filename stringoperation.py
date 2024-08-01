#replace                                                                                                                                                                                                                                                                                                                                                                                                                                                           #replace
a="it-is-an-apple"
b=a.replace("-"," ")
print(b)

#split
a="i@have@an@doubt"
print(a.split("@"))

#count
a="i want apple and the apple is sweet"
b=a.count("apple","mango")
print(b)

#reverse
x="ilikeapple"
print(x[::-1])

#join 
myvalues="what","is","your","name"
x="and".join(myvalues)
print(x)

#uppercase
a="bhavyadharshini"
print(a[::-1].upper())
a="bhavyadharshini"
b="inihsrahdayvahb"
name="this is {}, my name {}"
print(name.format(a,b))

#strip
a="**my name is python**"
a=a.strip("*")
print(a)
b="  it is an apple  "
b=b.strip()
print(b)

#check
a="bhavya dharshini"
print("dharshin"in a)
print("h"in a)

#place
a="hello world"
b="bhavya"
print(b[2])

#lowercase true
a="BHAVYA"
v=a.islower()
print(v)

#length
a="bhavyadharshini"
print(len(a))

#upper true
a="shiva"
b=a.isupper()
print(b)

#concatenate
a="bye"
b="hi"
c=a+v
print(c)

#format string
x="star"
a="the value is upper"
b="the value is lower between{}"
print(b.format(x))

#example
quantity=3
price=4
itemno=9
myorder="I want {} quantity, and{} pieces,{} itemno"
print(myorder.format(price,itemno,quantity))

#format method 2
a="myvalue"
b="livewire"
course="python"
hrs="sixty"
details=(
    f"{a}"
    f"{name}"
    f"{course}"
    f"{hrs}"
)
print(details)

#slicing
string="hello world"
a=slice(3)
b=slice(1,5,6)
c=slice(-1,-3,-5)
print(string[a])
print(string[b])
print(string[c])

#example
b="helloworld"
a=slice(4)
b=slice(1,5,6)
c=slice(-1,-3,-5)
print(string[a])
print(string[b])
print(string[c])

#example
string="livewire"
print(string[2:6])
print(string[:6])
print(string[3:])

#negative index
print(string[-5:-2])






















