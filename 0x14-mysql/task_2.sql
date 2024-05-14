-- creates a database and table with a single entry.

create database if not exists tyrell_corp;
use tyrell_corp;
create table if not exists nexus6
(
	id INT,
	name VARCHAR(256)
);
grant select on tyrell_corp.nexus6 to 'holberton_user'@'localhost';
insert into nexus6 (id, name) values(1, 'Leon');
