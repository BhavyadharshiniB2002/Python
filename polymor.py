
#Polymorphism
'''class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f"am a student.my name is {self.name}.am {self.age} years old")
    def info(self):
        print("marks")
class staff():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f"am a staff.my name is {self.name}.am {self.age} years old")
    def info(self):
        print("marks")
obj1=student("arsha",24)
obj2=staff("krish",40)
obj1.details()
obj1.info()
obj2.details()
obj2.info()'''

#example
'''class employee():
    def __init__(self,employeename,salary,qualification):
        self.employeename=employeename
        self.salary=salary
        self.qualification=qualification
    def details(self):
        print(f"am a employee{self.employeename},{self.salary},{self.qualification}")
class hr():
    def __init__(self,employeename,salary,qualification):
        self.employeename=employeename
        self.salary=salary
        self.qualification=qualification
    def details(self):
        print(f"am a employee{self.employeename},{self.salary},{self.qualification}")
obj=employee("bhavya",23455,"b.sc")
obj2=hr("abi",23145,"m.sc")
obj.details()
obj2.details()'''

# #super function
#It is used to direct use child class parameters without parent class
'''class parent():
    def fun(self):
        print("they are aprent of arshi:")
class child(parent):
    def fun1(self):
        super().fun()
        print("theya re the best parent")
obj=child()
obj.fun1()'''

#abstract method
'''from abc import ABC, abstractmethod
class bank(ABC):
    def bank_info(self):
        print("welcome to bank")
    @abstractmethod
    def interest(self):
        "abstract method"
        pass
class SBI(bank):
    def interest(self):
        print("5 percentage")
s=SBI()
s.bank_info()
s.interest()'''
