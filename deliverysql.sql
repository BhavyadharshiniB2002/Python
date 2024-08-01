show databases;
create database delivery;
use delivery;
create table order1 (name varchar(30),mobileno varchar(20),address varchar(20),paymentmode varchar(30));
insert into order1 values("sheela","9626513257","myd","cashondelivery");
insert into order1 values("bhavya","9626500007","kali","paytm");
select * from order1;

