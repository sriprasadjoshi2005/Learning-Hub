---
title: Database Fundamentals and DBMS
level: foundation
---

A database is an organized collection of information that can be stored, retrieved, updated, and managed efficiently. Database systems are essential to websites, banking applications, healthcare systems, business software, and modern information technology.

## 1. Understanding Databases

A database stores related information in an organized manner.

Examples include:

- Student records.
- Banking transactions.
- Product inventories.
- Employee information.
- Hospital patient records.
- Online shopping orders.

Databases make it easier to manage large amounts of information.

## 2. Database Management System

A Database Management System, or DBMS, is software used to create, organize, retrieve, update, and manage databases.

Its responsibilities commonly include:

- Data storage.
- Data retrieval.
- Data modification.
- Access control.
- Data integrity.
- Backup and recovery.
- Concurrency management.

Examples of DBMS software include:

- MySQL.
- PostgreSQL.
- SQLite.
- Oracle Database.
- Microsoft SQL Server.

## 3. Database vs DBMS

| Database | DBMS |
| --- | --- |
| Organized collection of data | Software that manages databases |
| Contains stored information | Provides operations on stored information |
| Represents the data itself | Provides the management environment |

A database and a DBMS are related but are not the same thing.

## 4. File Systems and Databases

Traditional file systems store information in individual files.

Database systems provide more structured management.

| Feature | File System | DBMS |
| --- | --- | --- |
| Organization | Files and folders | Structured database |
| Relationships | Often managed manually | Can be represented directly |
| Querying | Requires custom processing | Supports query languages |
| Data Integrity | Application-dependent | Supports integrity constraints |
| Concurrent Access | More difficult to coordinate | Provides concurrency mechanisms |
| Security | File-level controls | Database-level permissions |

A DBMS is particularly useful when information must be shared and managed consistently by multiple applications or users.

## 5. Relational Databases

A relational database organizes data into tables.

A table contains:
- Rows: Individual records.
- Columns: Attributes or fields.

Example:

| Student_ID | Name | Age |
| --- | --- | --- |
| 101 | Asha | 20 |
| 102 | Ravi | 21 |
| 103 | Meera | 19 |

Each row represents a student, while each column represents an attribute.

## 6. Database Keys

Keys identify records and establish relationships between tables.

### Primary Key

A primary key uniquely identifies each record in a table.

A primary key must be unique and cannot contain NULL values.

Example: Student_ID.

### Foreign Key

A foreign key is a field that references a key in another table or, in some designs, the same table.

It establishes relationships between records.

### Candidate Key

A candidate key is a minimal set of attributes capable of uniquely identifying a record.

A table may have multiple candidate keys.

### Composite Key

A composite key consists of two or more attributes used together to identify a record uniquely.

## 7. Relationships Between Tables

Relational databases support different relationship types.

### One-to-One

One record in a table is associated with at most one corresponding record in another table.

### One-to-Many

One record in a table can be associated with multiple records in another table.

Example: One department may have many employees.

### Many-to-Many

Multiple records in one table can relate to multiple records in another table.

Example: Students can enroll in multiple courses, and courses can contain multiple students.

A junction table is commonly used to implement a many-to-many relationship.

## 8. Database Schemas

A database schema describes the structure and organization of a database.

It may specify:

- Tables.
- Columns.
- Data types.
- Keys.
- Constraints.
- Relationships.
- Indexes.

A schema provides a structural plan for storing information.

## 9. Data Integrity

Data integrity refers to the accuracy, consistency, and validity of stored information.

Important constraints include:

- PRIMARY KEY: Enforces unique identification.
- FOREIGN KEY: Enforces referential relationships.
- NOT NULL: Prevents missing values in a column.
- UNIQUE: Prevents duplicate values.
- CHECK: Enforces a specified condition.
- DEFAULT: Supplies a default value when one is not provided.

Constraints help prevent invalid data from entering a database.

## 10. Types of DBMS

### Relational DBMS

Stores information in related tables.

Examples:
- MySQL.
- PostgreSQL.
- SQLite.

### Hierarchical DBMS

Organizes information in a tree-like parent-child structure.

### Network DBMS

Organizes records using interconnected relationships.

### Object-Oriented DBMS

Stores information using object-oriented concepts.

### NoSQL Databases

Supports data models that are not restricted to traditional relational tables.

Examples include document, key-value, column-family, and graph databases.

## 11. Database Transactions

A transaction is a logical unit of database operations treated as a single operation.

For example, transferring money between two accounts may involve:

1. Subtracting money from one account.
2. Adding money to another account.

Both operations should succeed together or be rolled back to preserve consistency.

## 12. ACID Properties

Database transactions are commonly described using ACID properties.

| Property | Meaning |
| --- | --- |
| Atomicity | All operations succeed or none are applied |
| Consistency | A transaction preserves database rules |
| Isolation | Concurrent transactions are controlled to prevent improper interference |
| Durability | Committed changes survive system failures according to the database's durability guarantees |

These properties support reliable transaction processing.

## 13. Database Applications

Databases are used in:

- Banking systems.
- E-commerce platforms.
- University management.
- Hospital information systems.
- Inventory management.
- Social networking.
- Reservation systems.
- Financial applications.

## Common Exam Traps

- A DBMS is software used to manage databases.
- A relational database stores information in tables.
- Rows represent records, while columns represent attributes.
- A primary key uniquely identifies a record and cannot be NULL.
- A foreign key establishes a reference to another key.
- Many-to-many relationships are commonly implemented using a junction table.
- A schema describes database structure.
- ACID stands for Atomicity, Consistency, Isolation, and Durability.

## Quiz

1. What does DBMS stand for?
   - [ ] Data Backup Management System
   - [x] Database Management System
   - [ ] Digital Binary Management Software
   - [ ] Database Memory Structure

   > A DBMS is software that manages the creation, storage, retrieval, and modification of databases.

2. Which key uniquely identifies each record in a table?
   - [ ] Foreign key
   - [ ] Composite attribute
   - [x] Primary key
   - [ ] Duplicate key

   > A primary key uniquely identifies records and cannot contain NULL values.

3. Which ACID property ensures that a transaction is treated as an all-or-nothing operation?
   - [ ] Durability
   - [ ] Consistency
   - [x] Atomicity
   - [ ] Isolation

   > Atomicity ensures that all operations in a transaction succeed together or none are applied.