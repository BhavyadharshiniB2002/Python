#show connection object
'''import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="user1")
print(connection)'''

#create database
'''import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("create database python")'''


#show all database with in root user
'''import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",passwordd="livewire")
cursor=connection.cursor()
cursor.execute("show databases")
for x in cursor:
    print(x)'''

#create table
'''import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="python") 
cursor=connection.cursor()
cursor.execute("create table departments(dep_id int primary key, dep_name varchar(50))")
cursor.execute("show tables")
print("number of tables in database:")
for x in cursor:
    print("/t",x)'''

'''import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="python")
cursor=connection.cursor()
cursor.execute("create table employees(emp_id int primary key, emp_name varchar(50))")
cursor.execute("show tables")
print("number of tables in database:")
for x in cursor:
    print("/t",x)'''

''' import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="python")
cursor=connection.cursor()
s="insert into employees values(%s,%s)"
t=(1,"abi")
cursor.execute(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid)'''

# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire",database="python")
# cursor=connection.cursor()
# s="insert into employees values(%s,%s)"
# t=[(2,"harish",),(3,"harish")]
# cursor.executemany(s,t)
# connection.commit()
# print(cursor.rowcount,"new row inserted",cursor.lastrowid)

# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire",database="python")
# cursor=connection.cursor()
# cursor.execute("select*from employees")
# result=cursor.fetchall()
# print("content in the python:")
# for x in result:
#     print("/t",x)

# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire",database="python")
# cursor=connection.cursor()
# sql="update employees set emp_name='bhavya' where emp_id=1;"
# cursor.execute(sql)
# connection.commit()
# print("updated in python",sql)

# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire",database="python")
# cursor=connection.cursor()
# sql="delete from employees where emp_id=1"
# cursor.execute(sql)
# connection.commit()
# print(cursor.rowcount,"record(s)deleted")

# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire")
# cursor=connection.cursor()
# #cursor.execute("create database user1")
# cursor.execute("show databases")
# for x in cursor:d
#     print(x)
# cursor.execute("use python")
# #cursor.execute("create table departments(dep_id int primary key, dep_name varchar(50))")
# cursor.execute("show tables")
# print("number of tables in database:")
# for x in cursor:
#     print("/t",x)
# s="insert into departments values(%s,%s)"
# t=(2,"harish")
# cursor.execute(s,t)
# connection.commit()
# print(cursor.rowcount,"new row inserted",cursor.lastrowid)
# cursor.execute("select*from departments")
# result=cursor.fetchall()
# print("content in the python:")
# for x in result:
#     print("/t",x)
# sql="update departments set dep_name='bhavya' where dep_id=1;"
# cursor.execute(sql)
# connection.commit()
# sql="delete from departments where dep_id=1"
# cursor.execute(sql)
# connection.commit()
# print(cursor.rowcount,"record(s)deleted")


