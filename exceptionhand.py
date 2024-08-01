
#exception handling
try:
    file1=open("new.txt","r")
    print(file1.read())
    file1.close()
except FileNotFoundError:
    print("filenot found errorsuccessfully handled")
          
