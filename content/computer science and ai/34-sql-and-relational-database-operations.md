---
title: SQL and Relational Database Operations
level: intermediate
---

SQL, or Structured Query Language, is a standard language used to communicate with relational database systems. It allows users to create database structures, retrieve information, modify records, and control access.

## 1. Understanding SQL

SQL is used to interact with relational databases.

Common applications include:

- Retrieving customer information.
- Adding new records.
- Updating product prices.
- Removing obsolete data.
- Creating tables.
- Managing database permissions.
- Performing calculations on stored records.

Different database systems implement SQL with some variations.

## 2. Categories of SQL Commands

SQL commands are commonly grouped into categories.

| Category | Purpose | Examples |
| --- | --- | --- |
| DDL | Defines database structures | CREATE, ALTER, DROP |
| DML | Modifies stored data | INSERT, UPDATE, DELETE |
| DQL | Retrieves information | SELECT |
| DCL | Controls access permissions | GRANT, REVOKE |
| TCL | Manages transactions | COMMIT, ROLLBACK, SAVEPOINT |

## 3. Creating a Table

The CREATE TABLE command creates a new table.

Example:

```sql
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    department VARCHAR(50)
);
```

This creates a table containing student information.

## 4. Inserting Records

The INSERT command adds new records.

Example:

```sql
INSERT INTO Students (student_id, name, age, department)
VALUES (101, 'Asha', 20, 'Computer Science');
```

Multiple records can also be inserted in a single statement.

## 5. Retrieving Data

The SELECT statement retrieves information.

Example:

```sql
SELECT * FROM Students;
```

The asterisk represents all columns.

To retrieve selected columns:

```sql
SELECT name, department
FROM Students;
```

## 6. Filtering with WHERE

The WHERE clause filters records according to a condition.

Example:

```sql
SELECT *
FROM Students
WHERE age > 20;
```

Common comparison operators include:

| Operator | Meaning |
| --- | --- |
| = | Equal |
| != | Not equal |
| <> | Not equal |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |

## 7. Logical Operators

SQL supports logical operators for combining conditions.

### AND

All specified conditions must be true.

```sql
SELECT *
FROM Students
WHERE age >= 18 AND department = 'Computer Science';
```

### OR

At least one condition must be true.

```sql
SELECT *
FROM Students
WHERE department = 'Computer Science'
OR department = 'Mathematics';
```

### NOT

Reverses a condition.

```sql
SELECT *
FROM Students
WHERE NOT department = 'Physics';
```

## 8. Sorting with ORDER BY

ORDER BY arranges query results.

Example:

```sql
SELECT *
FROM Students
ORDER BY age ASC;
```

ASC means ascending order.

DESC means descending order.

Example:

```sql
SELECT *
FROM Students
ORDER BY age DESC;
```

## 9. Updating Records

The UPDATE command modifies existing records.

Example:

```sql
UPDATE Students
SET age = 22
WHERE student_id = 101;
```

The WHERE clause identifies which records should be updated.

Without an appropriate WHERE clause, every record in the table may be modified.

## 10. Deleting Records

The DELETE command removes records.

Example:

```sql
DELETE FROM Students
WHERE student_id = 101;
```

Without a WHERE clause, all rows may be deleted.

The table structure remains.

## 11. Aggregate Functions

Aggregate functions perform calculations over groups of records.

| Function | Purpose |
| --- | --- |
| COUNT() | Counts records or values |
| SUM() | Calculates a total |
| AVG() | Calculates an average |
| MIN() | Finds the minimum |
| MAX() | Finds the maximum |

Example:

```sql
SELECT AVG(age)
FROM Students;
```

This calculates the average age of the selected records.

## 12. GROUP BY

GROUP BY groups records that share specified values.

Example:

```sql
SELECT department, COUNT(*)
FROM Students
GROUP BY department;
```

This calculates the number of students in each department.

## 13. HAVING

HAVING filters groups after aggregation.

Example:

```sql
SELECT department, COUNT(*)
FROM Students
GROUP BY department
HAVING COUNT(*) > 5;
```

This returns departments containing more than five students.

## 14. SQL Joins

Joins combine related information from multiple tables.

Suppose there are two tables:

Students:

| student_id | name |
| --- | --- |
| 101 | Asha |
| 102 | Ravi |

Enrollments:

| enrollment_id | student_id | course |
| --- | --- | --- |
| 1 | 101 | Mathematics |
| 2 | 102 | Physics |

### INNER JOIN

Returns records with matching values in both tables.

```sql
SELECT Students.name, Enrollments.course
FROM Students
INNER JOIN Enrollments
ON Students.student_id = Enrollments.student_id;
```

### LEFT JOIN

Returns all records from the left table and matching records from the right table.

Unmatched right-side values are represented by NULL.

### RIGHT JOIN

Returns all records from the right table and matching records from the left table.

### FULL OUTER JOIN

Returns matching records and unmatched records from both sides.

Support for FULL OUTER JOIN varies between database systems.

## 15. Subqueries

A subquery is a query placed inside another SQL statement.

Example:

```sql
SELECT name
FROM Students
WHERE age > (
    SELECT AVG(age)
    FROM Students
);
```

This retrieves students whose ages exceed the average age.

## 16. SQL Constraints

Constraints enforce rules on stored data.

Common constraints include:

- PRIMARY KEY.
- FOREIGN KEY.
- NOT NULL.
- UNIQUE.
- CHECK.
- DEFAULT.

They help preserve database integrity.

## 17. SQL Transactions

Transactions allow related database operations to be managed together.

Common commands include:

- COMMIT: Permanently saves transaction changes.
- ROLLBACK: Reverses uncommitted changes.
- SAVEPOINT: Creates a point to which a transaction can be rolled back.

## 18. SQL Best Practices

- Use meaningful table and column names.
- Specify columns explicitly when practical.
- Use WHERE carefully in UPDATE and DELETE statements.
- Use constraints to protect data integrity.
- Avoid unnecessary retrieval of all columns.
- Use parameterized queries in applications to prevent SQL injection.
- Use transactions for related operations that must remain consistent.

## Common Exam Traps

- SELECT retrieves records.
- INSERT adds records.
- UPDATE modifies records.
- DELETE removes records without removing the table structure.
- DROP removes a database object.
- WHERE filters individual records.
- HAVING filters groups.
- GROUP BY creates groups for aggregate calculations.
- INNER JOIN returns matching rows.
- LEFT JOIN preserves all rows from the left table.
- COMMIT saves transaction changes, while ROLLBACK reverses uncommitted changes.

## Quiz

1. Which SQL command retrieves records from a table?
   - [ ] UPDATE
   - [ ] INSERT
   - [x] SELECT
   - [ ] DROP

   > SELECT retrieves information from database tables.

2. Which clause filters groups after aggregate calculations?
   - [ ] WHERE
   - [ ] ORDER BY
   - [x] HAVING
   - [ ] INSERT

   > HAVING applies conditions to grouped results.

3. Which join preserves every row from the left table?
   - [ ] INNER JOIN
   - [ ] RIGHT JOIN
   - [ ] CROSS JOIN
   - [x] LEFT JOIN

   > LEFT JOIN returns all left-table records and matching right-table records.