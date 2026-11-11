---
title: Database Normalization and Advanced Concepts
level: advanced
---

Database normalization is the process of organizing relational database tables to reduce unnecessary duplication and improve data integrity. It is an important part of database design and helps prevent problems when information is inserted, updated, or deleted.

## 1. Understanding Database Redundancy

Data redundancy occurs when the same information is stored repeatedly.

Consider a table containing student names, courses, and department details.

| Student_ID | Student_Name | Department | Course |
| --- | --- | --- | --- |
| 101 | Asha | Computer Science | Programming |
| 101 | Asha | Computer Science | Mathematics |
| 102 | Ravi | Electronics | Circuits |

Department information is repeated whenever a student appears in multiple records.

Unnecessary duplication can increase storage requirements and create inconsistencies.

## 2. Database Anomalies

Poorly designed tables can produce three important anomalies.

### Insertion Anomaly

Occurs when information cannot be inserted without adding unrelated information.

Example: A new department cannot be recorded until at least one student is assigned to it.

### Update Anomaly

Occurs when the same information appears in multiple records and every copy must be updated.

If a department name changes, several rows may need modification.

### Deletion Anomaly

Occurs when deleting one record unintentionally removes other valuable information.

For example, deleting the only student associated with a department may also remove the only stored record of that department.

Normalization helps reduce these problems.

## 3. Functional Dependencies

A functional dependency describes a relationship between attributes.

It is written as:

A -> B

This means that attribute A determines attribute B.

For example:

Student_ID -> Student_Name

This means that each Student_ID identifies one corresponding student name, assuming Student_ID is unique.

Functional dependencies are important for determining suitable table structures.

## 4. First Normal Form

First Normal Form, or 1NF, requires that:

- Each field contains a single value from its defined domain.
- Repeating groups are eliminated.
- Each record can be distinguished appropriately.

A table should not store multiple unrelated values inside one ordinary field.

Example of a non-atomic field:

| Student_ID | Phone_Numbers |
| --- | --- |
| 101 | 9876, 8765 |

A better design stores individual phone numbers in separate rows or in a related table, depending on the requirements.

## 5. Second Normal Form

Second Normal Form, or 2NF, requires:

- The table must satisfy 1NF.
- Every non-prime attribute must depend on the whole of every candidate key, not merely part of a composite candidate key.

A partial dependency occurs when a non-key attribute depends on only part of a composite candidate key.

For example, consider an enrollment table whose key is:

(Student_ID, Course_ID)

If Student_Name depends only on Student_ID, it is partially dependent on the composite key.

Student information should be separated into an appropriate student table.

## 6. Third Normal Form

Third Normal Form, or 3NF, requires:

- The table must satisfy 2NF.
- Non-key attributes must not have inappropriate transitive dependencies on candidate keys.

A transitive dependency occurs when a key determines one non-key attribute, which in turn determines another non-key attribute.

Example:

Student_ID -> Department_ID

Department_ID -> Department_Name

Instead of repeatedly storing department names in student records, department information can be placed in a separate department table.

## 7. Boyce-Codd Normal Form

Boyce-Codd Normal Form, or BCNF, is a stronger form of 3NF.

A relation satisfies BCNF when every non-trivial functional dependency has a superkey as its determinant.

A superkey is a set of attributes capable of uniquely identifying a record.

BCNF addresses certain dependency problems that can remain in relations satisfying 3NF.

## 8. Normalization Summary

| Normal Form | Main Requirement |
| --- | --- |
| 1NF | Atomic field values and no repeating groups |
| 2NF | 1NF and no partial dependency of non-prime attributes on candidate keys |
| 3NF | 2NF and no prohibited transitive dependency of non-prime attributes |
| BCNF | Every determinant of a non-trivial functional dependency is a superkey |

Each successive form imposes stronger structural requirements.

## 9. Database Denormalization

Denormalization intentionally introduces some redundancy into a database.

It may be used to improve read performance or simplify certain queries.

Examples include:

- Storing calculated summary values.
- Duplicating selected information.
- Combining tables for frequently accessed reports.

Denormalization can improve performance but increases the responsibility for maintaining consistency.

## 10. Database Indexing

An index is an additional data structure that helps a database locate records more efficiently.

Without an appropriate index, a database may need to scan many records.

Indexes can improve query performance, especially for frequently searched columns.

However, indexes also have costs:

- Additional storage.
- Slower insertion operations in some cases.
- Slower updates and deletions when indexed values change.
- Maintenance overhead.

Common index structures include B-trees and hash-based indexes.

## 11. Database Views

A view is a virtual table defined by a query.

Example:

```sql
CREATE VIEW ComputerScienceStudents AS
SELECT student_id, name
FROM Students
WHERE department = 'Computer Science';
```

A view can simplify repeated queries and restrict which columns or records are exposed to particular users.

Some database systems also support materialized views, which store query results physically and require refresh management.

## 12. Database Transactions and Concurrency

Multiple users may access a database simultaneously.

Concurrency control helps ensure that simultaneous operations do not produce invalid results.

Important problems include:

- Lost updates.
- Dirty reads.
- Non-repeatable reads.
- Phantom reads.

Database systems use locking, multiversion concurrency control, and transaction isolation mechanisms to manage these situations.

## 13. Backup and Recovery

Database backup creates a recoverable copy of stored information.

Recovery procedures restore the database after failures.

Common approaches include:

- Full backups.
- Incremental backups.
- Differential backups.
- Transaction logs.
- Point-in-time recovery.

A backup strategy should be tested regularly rather than merely assumed to work.

## 14. Choosing a Database Design

A suitable database design considers:

- Data relationships.
- Expected queries.
- Integrity requirements.
- Transaction behaviour.
- Storage requirements.
- Performance.
- Security.
- Future changes.

Normalization is a foundation for reliable relational design, while indexing and carefully chosen denormalization can improve practical performance.

## Common Exam Traps

- Normalization reduces unnecessary redundancy.
- 1NF requires atomic values and the elimination of repeating groups.
- 2NF eliminates partial dependencies of non-prime attributes on candidate keys.
- 3NF addresses transitive dependencies of non-prime attributes.
- BCNF requires every determinant of a non-trivial functional dependency to be a superkey.
- Denormalization deliberately introduces redundancy.
- Indexes improve certain retrieval operations but require additional storage and maintenance.
- A view is defined by a query.
- Concurrency control manages simultaneous database operations.

## Quiz

1. Which normal form requires the elimination of partial dependencies of non-prime attributes on candidate keys?
   - [ ] 1NF
   - [x] 2NF
   - [ ] 3NF
   - [ ] BCNF

   > Second Normal Form requires 1NF and removes partial dependencies.

2. What is the primary purpose of a database index?
   - [ ] To eliminate every duplicate value
   - [ ] To replace the database schema
   - [x] To improve the efficiency of locating records
   - [ ] To automatically normalize every table

   > An index helps the database locate relevant records without scanning the entire table in many cases.

3. What does denormalization intentionally introduce in some database designs?
   - [ ] Mandatory deletion
   - [ ] Removal of all indexes
   - [x] Controlled data redundancy
   - [ ] Elimination of primary keys

   > Denormalization may introduce controlled redundancy to improve read performance or simplify queries.