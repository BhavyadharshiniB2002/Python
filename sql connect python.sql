show databases;
create database banksql;
use banksql;
show tables;
create table employees(name varchar(20),adharno int(30),panno int(30),contact varchar(30),emailid varchar(30),address varchar(40));
insert into employees(name, adharno, panno, contact, emailid, Address)values("bhavya",12345,12345,12345,"bhavya12345","mayiladuthurai");
insert into employees(name, adharno, Panno, contact, emailid, Address)values("abi",1111,1111,1111,"gggg","dddd");
select*from employees;



