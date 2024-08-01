#file handling
#openfile #r-read operation
file=open("new.txt","r")
for each in file:
    print(each)

#method2
file=open("word.txt","r")
print(file.read())

#method
#with statement
with open("new.txt") as file:
    data=file.read()
print(data)

#read count letters
file=open("new.txt","r")
print(file.read(14))

#create new file
file=open("new.txt","w")
file.write("\nemp name\tage\tsalary\tqualifi")
file.write("\nanbu\t23\t2000\tdme")
file.write("\nakash\t21\t3000\tb.sc")
file.write("\nbijorn\t24\t4000\tdme")
file.write("\nvishwa\t20\t1000\tdme")
file.write("\najay\t21\t1200\tb.com")
file.close()

file=open("new.txt","w")
file.write("hii")
file.close()

#write with new file
file=open("new.txt","w")

#append
file=open("new.txt","a")
file.write("This will add this line")
file.close()
myfile=open("bhavyafile.txt","r")
myfile=open("bhavyafile.txt","r")

#write file
file=open("new.txt","w")
l=["This is delhi\n","This is paris\n","This is london"]
file.writelines(l)
file.close()

#append file
file1=open("bhavyafile.txt","a")
file1.write("hii kirthika\n")
file1.close()

#run on output view
file1=open("bhavyafile.txt","r")
print("output of readlines after appending")
print("please enter your data:","r")
print("please enter your data:","a")
print(file1.read())
print()
file1.close()

a=["This is Delhi \n","This is paris \n","This is london\n"] with open("bhavyafile.txt","w") as file1:
file1.write("The statement of the view... with alone be the best")
file1.writelines(a)

#with open file
with open("bhavyafile.txt","a")as file1:
    file1.write("Today")
with open("bhavyafile.txt","r")as file1:
    print(file1.read())

#file open
file=open("test.txt","w")
file.write("Hello World")
file.seek(0)
data=file.read()
print(data)
file.close()

#example
name=open("data.txt","a")
name.write("The data are stored to content\n")
name.write("employee name\tsalary\tdesignationaddress\t\n")
name.write("Muruga\t\t\t10000\tBE\tmyd\n")
name.write("Livewire\t3000\tno\tmyd\t")
name.close()
name=open("data.txt","r")
print(name.read(12))
with open("data.txt")as name:
    data=name.read()
print(data)



#Delete
import os
if os.path.exists("new.py"):
    os.remove("new.py")
    print("File deleted")
else:
    print("File doesnot deleted")

