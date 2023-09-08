create database lmsdb;
use lmsdb;

create table person(
person_id int not null auto_increment,
username nvarchar(30) not null,
email nvarchar(30),
password nvarchar(250) not null,
bdate date,

primary key (person_id)
);
drop table subjects
create table subjects(
sub_id int not null auto_increment, 
sub_name nvarchar(50),
primary key(sub_id)
);
alter table ccolumn sub_id 

create table courses(
course_no int not null auto_increment,
title TEXT not null,
Primary key (course_no)
); 
drop table course_info;
create table course_info(
course_info_id int  not null,
course_no int not null,
intro text,
description text,
subjects int not null,
primary key(course_info_id),
foreign key(course_no) references courses(course_no) on update cascade on delete cascade,
foreign key(subjects) references subjects(sub_id) on update cascade on delete cascade
);

select sub_name from subjects

insert into subjects (sub_name) values 
("Python"),
("c++"),
("Accounting"),
("Web Development")





select * from person;
select * from subjects; 
select * from courses; 
select * from course_info;