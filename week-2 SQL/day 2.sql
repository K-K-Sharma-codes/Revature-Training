use Revstuddb;
begin transaction;

insert into dbo.student values(101,'AAA','pg','BLR',990532);
insert into dbo.student (rollno,sname,pin)
values(105,'BBB',9674634);



insert into dbo.student (rollno,pin,sname)
values(107,9674634,'BBB');

update student set addr ='grd'
where rollno=107;

SAVE TRANSACTION savepoint_name;

ROLLBACK TRANSACTION savepoint_name; 

insert into dbo.student (rollno,sname,pin)
values(109,'BBB',9674634);
insert into dbo.student (rollno,sname,pin)
values(115,'BBB',9674634);

commit transaction

delete from student where rollno=105;

truncate table student;

select * from student;

create database RevCompanyDb;

use RevCompanyDb;

create table dept(deptno smallint,dname  varchar (3) not null,
constraint pk_deptno primary key(deptno));



create table emp(empno smallint,
ename varchar(30) not null,
mgr smallint,
sal numeric(10,2),
comm numeric(7,2),
deptno smallint,
constraint pk_empno primary key(empno),
constraint fk_deptno foreign key (deptno) references dept(deptno));

insert into dept values(10,'IT')
insert into dept values(20,'HR')
insert into dept values(30,'SAL')
insert into dept values(60,'MKT')
insert into dept values(70,'OPS')

INSERT INTO 
emp (empno, ename, mgr, sal, comm, deptno) 
VALUES
(1001, 'Alice', NULL, 60000.00, NULL, 10), 
(1002, 'Bob', 1001, 75000.00, NULL, 20),   
(1003, 'Charlie', 1002, 50000.00, 500.00, 30),
(1004, 'Diana', 1003, 52000.00, 300.00, 60), 
(1005, 'Ethan', 1002, 58000.00, NULL, 70), 
(1006, 'Fiona', 1005, 62000.00, NULL, 60); 

select * from emp;


select *
from emp

select empno as "Emp Num",ename as "Name"
from emp
where sal>60000

select empno as "Emp Num",ename as "Name",sal as "salary"
from emp
where empno!=1004 and empno!=1003

select empno as "Emp Num",ename as "Name",sal as "salary"
from emp
where empno in(1002,1003,1004)

select empno as "Emp Num",ename as "Name",sal as "salary"
from emp
where empno not in(1002,1003,1004)

select empno as "Emp Num",ename as "Name",sal as "salary"
from emp
where sal between 40000 and 55000

select empno as "Emp Num",ename as "Name",sal as "salary"
from emp
where ename LIKE '__a%'

select empno as "Emp Num",ename as "Name",sal as "salary"
from emp
where ename LIKE '[aE]%'

select empno as "Emp Num",ename as "Name",sal as "salary"
from emp
where empno=1004 and ename like '%a%';

select empno as "Emp Num",ename as "Name",sal as "salary"
from emp
where empno != 1003;

select empno as "Emp Num",ename as "Name",sal as "salary"
from emp
where sal > 50000
order by salary Desc;

select empno as "Emp Num",ename as "Name",sal as "salary",comm as "Commision"
from emp
where sal>50000
order by comm,sal desc

select count(empno) as 'No of employee',sum(sal) as 'Total',avg(comm) as 'Avg comm',
min(sal) as 'Least sal',max(sal) as 'Top earner'
from emp

select deptno as 'Department',sum(sal) as 'Total Salary'
from emp
group by deptno
having deptno in(10,20,30)

select deptno as 'Department',sum(sal) as 'Total Salary'
from emp
where	deptno in (10,20,30)
group by deptno

select deptno as 'Department',sum(sal) as 'Total Salary'
from emp
group by deptno
having sum(sal) >=75000

select e.ename,d.dname
from emp e left join dept d
on d.deptno =e.deptno;

select e.ename,d.dname
from emp e inner join dept d
on d.deptno =e.deptno;

select e.ename,d.dname
from emp e left outer join dept d
on d.deptno =e.deptno;

select e.ename,d.dname
from emp e full outer join dept d
on d.deptno =e.deptno;