 #for loop           
a="bhavya"
for i in a:
    print(i)

#range in for
for x in range(1,20,3):
    print(x)

#list in for
a=["happy",2,6]
for i in a:
    print(i)
list1=[1,2,3,4]
sum=0
for i in list1:
    sum=sum+i
    print("the total value is:",sum)

#continue
for x in range(5):
    if(x==20):
        continue
    print(x)

#Break
for x in range(25):
    if(x==20):
        break
    print(x)

#pass
for x in range(25):
    if(x==20):
        pass
