show databases;
create database user1;
use user1;
show tables;
create table t1 (sno int not null auto_increment primary key,sname varchar(255),m1 int(10),m2 int(10),m3 int(10),m4 int(10),m5 int(10));
insert into t1 (sname)values("bhavya");
insert into t1 (sname)values("abi");
insert into t1 (m1)values("50","50");
insert into t1 (m2)values("50","50");
insert into t1 (m3)values("50","50");
insert into t1 (m4)values("50","50");
insert into t1 (m5)values("50","50");
select * from t1;
insert into t1 (sname)values("bhavya");
select sname from t1 where sno=2;
select sname from t1 where sno=3;


