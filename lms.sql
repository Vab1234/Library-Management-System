drop database if exists sms;
create database sms;
use sms;

create table books(
book_id int primary key,
name varchar(50) not null,
publisher_name varchar(50),
`issued?` int not null default 0);


create table students(
id int primary key,
name varchar(50) not null,
class varchar(10) not null,
branch varchar(50) not null,
book_issued int,
issued date date,
foreign key students(book_issued) references books(book_id));

desc students;
desc books;
