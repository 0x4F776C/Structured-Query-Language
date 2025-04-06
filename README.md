# Structured-Query-Language
Can't wait for the SQL of this movie!

<!-- display-subdirectories: false -->

# Introduction to SQL

*This document will contain all the basic knowledge needed to excel in your upcoming courses!*

## What is SQL?

* SQL stands for Structured Query Language

* SQL is a language for manipulating databases such as MSSQL and MySQL

### What can SQL do for You?

1. Create data
2. Read data
3. Update data
4. Delete data

You will see this acronym very often - *CRUD*

## What is a Database?

* Database is an organized collection of structured information, or data, usually stored electronically in a digital system.

### Types of Databases

1. Centralized database
2. Distributed database
3. Personal database
4. End-user database
5. Commercial database
6. NoSQL database
7. Operational database
8. Relational database
9. Cloud database
10. Object-oriented database
11. Graph database

*We can ignore most of them for now as we will only be focusing on manipulating relational database through the use of a relational database management system (RDBMS) called **MySQL**.*

#### What is MySQL?

> MySQL is an open-source RDBMS. It organizes data into one or more data tables in which their data types may be related to each other.

> MySQL can be integrated with an operating system to implement a relational database in a computer's storage system, allows for network access, managing users and facilitates testing database integrity and creation of backups.

## Diving into Basics

RDBMS contains one or more objects called tables. Tables are uniquely identified by their names and are comprised of columns and rows.

Columns - contain column name, data type, and other attributes for the column

Rows - contain records or data for the columns

`Sample table called 'Buffet'`

| Ranking | Name | Price (SGD) | Must Tries |
| --- | --- | --- | --- |
| 1 | Ikoi Japanese Restaurant | $38 - S50 | Sashimi, Sushi, Tempura, and Salmon Skin Temaki |
| 2 | Irodori Japanese Restaurant | $36.80++ | Sashimi, Maki, Tempura, Chawanmushi, Pork Roll with Golden Mushroom , and Crisp Nasu Miso Itame |
| 3 | Kuishin Bo Japanese Buffet Restaurant | [Varies](https://www.thebestsingapore.com/eat-and-drink/the-5-best-japanese-buffet-restaurants-in-singapore/) | Hokkaido Snow Crab, Sashimi, Prawn, Teppanyaki Beef Cubes, Tempura, Chocolate, and Soft Serve Ice Cream |

### Creating Table

The **create table** statement is used to create new table:

```sql
# create "Buffet" table

create table Buffet (Ranking number(2), Name varchar(20), Price varchar(100), "Must Tries" varchar(60));
```

#### Common Data Types

`Table containing common data types and  description`

| Data Type | Description |
| --- | --- |
| char(size) | Fixed-length character string. Size is specified in parenthesis. Max 255 bytes |
| varchar(size) | Variable-length character string. Max size is specified in parenthesis |
| number(size) | Number value with a max number of column digits specified in parenthesis |
| date | Date value |
| number(size, d) | Number value with a maximum number of digits of "size" total, with a maximum number of "d" digits to the right of the decimal |

#### Additional Data Types

* constraints - a rule associated to a column that the data must follow. No two records can have the same value
	* primary key - defines an unique identification of each record (or row) in a table
	* not null - column cannot be left blank

### Selecting Data

The **select** statement is used for querying data in a database:

```sql
# query all data from "Buffet" table

SELECT * from Buffet;

# query "Name" from "Buffet" table

SELECT Name from Buffet;

# query both "Name" and "Price" from "Buffet" table

SELECT Name, Price from Buffet;

# query "Name" from "Buffet" table where "Price" is lower than "$38" (do note that this query is invalid as table data contains symbols)

SELECT Name from Buffet
	WHERE Price < 38;
	
# query "Must Tries" and retrieve "Name" where data match "shimi" in "Buffet" table

SELECT Name from Buffet
	WHERE "Must Tries" LIKE "%shimi%";
```

### Inserting Data

The **insert** statement is used for inserting data in the database:

```sql
# insert "Chun Hao Free Restaurant" with "Ranking" of 7, "Price" of $0, and "Must Tries" of "Sashimi" in "Buffet" table

INSERT into Buffet (Ranking, Name, Price, "Must Tries")
	VALUES (7, "Chun Hao Free Restaurant", 0, "Sashimi");
```

### Updating Data

The **update** statement is used for updating data in the database:

```sql
# update "Must Tries" of "Chun Hao Free Restaurant" to "Yi Qian Free Restaurant" in "Buffet" table

UPDATE Buffet
	SET Name = "Yi Qian Free Restaurant"
	WHERE Ranking = 7;
```

### Deleting Data

The **delete** statement is used to delete data in the database:

```sql
# delete record where "Ranking" is 7 from "Buffet" table

DELETE from Buffet
	WHERE Ranking = 7;
```

### Drop Table

The **drop table** statement is used to drop table in the database:

```sql
# drop "Buffet" table

DROP TABLE Buffet;
```

---
End of summary - Basic

Do help yourself with the [intermediate tutorial](#References) if you can't wait!
---

# References
[W3Schools - SQL](https://www.w3schools.com/sql/default.asp)

[SQLCourse - Basic](http://www.sqlcourse.com/intro.html)

[SQLCourse - Intermediate](https://www.sqlcourse2.com/)
