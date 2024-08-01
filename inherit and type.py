#Inheritance (Reusability of code)

#single inheritance
'''class vehicle:
     def vehicle_info(self):
          print("inside vehicle class")
#child class
class car(vehicle):
     def car_info(self):
          print("inside car class")
#create object of car
car=car()
#access vehicles info using car object
car.vehicle_info()
car.car_info()'''

#multiple inheritance
'''class person():
     def person_info(self,name,age):
          print("inside person class")
          print("name:",name,"age",age)
#parent class 2
class company():
     def company_info(self,company_name,location):
          print("inside company class")
          print("name:",company_name,"location:",location)
#child class
class employee(person,company):
     def employee_info(self,salary,skill):
          print("inside employee class")
          print("salary:",salary,"skill:",skill)
#create object of employee
emp=employee()
#access data
emp.person_info("bhavya",23)
emp.company_info("fibro","myd")
emp.employee_info(2000,"machine learning")'''

#multiple inheritance
'''class student():
    def studentdetails(self):
        print("It is my details")
        print("It is my details")
class staff(student):
        def staffdetails(self):
            print("yeah its me")
detail=staff()
detail.studentdetails()
detail.staffdetails()'''

#multiple inheritance
'''class employeedetails():
     def company(self,name,age):
          print("It is my resume")
          print("name:",name,"age:",age)
class secondround():
     def round2(self,score):
          print("It is my score")
          print("my score is:",score)
class thirdround(employeedetails,secondround):
     def round3(self,hr):
          print("final round")
          print("my details",hr)
obj=thirdround()
obj.company("jith",23)
obj.round2(24)
obj.round3("sss")'''

'''class student():
    def stdname(self,name1):
      print("name:",name1)
class college(student):
   def clgname(self,name2):
      print("clgname:",name2)
class department(college):
   def depname(self,name3):
      print("depname:",name3)
project=department()
project.stdname("bhavya")
project.clgname("dgga")
project.depname("cs")'''

#Multiple Inheritance task

'''class covid19():
    def patients(self,count,certify):
        print("peoples affect in covid19:",count,certify)
class covid20():
    def patients2(self,count1,certify2):
        print(" peoples death in covid20:",count1,certify2)
        print(" peoples birth in covid20:",count1,certify2)
class covid21():
    def patients3(self,count3,certify3):
        print("peoples recovered in covid21:",count3,certify3)
class covid22(covid19,covid20,covid21):
    def patients4(self,count4,certify4):
        print("peoples are cured in covid22:",count4,certify4)
lockdown=covid22()
lockdown.patients(100,"positive")
lockdown.patients2(50,"positive")
lockdown.patients2(50,"negative")
lockdown.patients3(40,"positive")
lockdown.patients4("all","negative")'''

#Muliti level inheritance
'''class one():
    def name(self):
        print("am abhi")
class two(one):
    def age(self):
        print("am 23")
class three(two):
    def name3(self):
        print("from myd")
final=three()
final.name()
final.age()
final.name3()'''

#Hierarchical
'''class parent():
    def name(self):
        print("father name.krish")
class child1(parent):
    def childname(self):
   rint("child1 name is arsha")
class child2(parent):
    def child2name(self):
        print("child2 name is arshi")
obj=child1()
obj2=child2()
obj.name()
obj.childname()
obj2.child2name()'''

#Hybrid 

'''class name():
    def fun(self):
        print("hello this is abhi")
class name2(name):
    def fun1(self):
        print("hello this is asha")
class name3(name):
    def fun2(self):
        print("hello this is amir")
class name4(name):
    def fun3(self):
        print("hello this is bhavya")
obj=name4()
obj.fun()
obj.fun1(name)
obj.fun2(name)
obj.fun3'''

#example
'''
class bca():
    def bcastd(self,name,age):
        print("name:",name,"Age:",age)
class maths(bca):
    def mathstd(self,book,note):
        print("book:",book,)
class bcom(bca):
    def bcomstd(self,staff,hod):
        print("staff:",staff,"hod:",hod)
class bba(maths,bcom):
    def bbastd(self,accounts,commerce):
        print("acount:",accounts,"commerce:")
obj=bba()
obj=bcastd("mr",12)
obj.mathsstd("classmate","algebra)
obj.bcomstd("ms","kk")
obj.bbastd(1233,"sales")'''



    