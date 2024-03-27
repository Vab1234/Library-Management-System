drop database if exists student_record;
create database student_record;
use student_record;


create able student(
rno int primary key,
name varchar(50) not null,
marks int not null
);

desc student;

--To view issued books
--SELECT students.id, students.name, students.class, students.branch, books.name, students.issued_date FROM students INNER JOIN books on students.book_issued = books.book_id where books.`issued?` = 1

--To view books that are not issued
--select select * from books where books.`issued?` = 0


