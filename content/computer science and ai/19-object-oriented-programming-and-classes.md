---
title: Object-Oriented Programming and Classes
level: intermediate
---

Object-Oriented Programming (OOP) is a programming paradigm that organises software around objects containing data and related behaviour. It provides a structured approach to building reusable and maintainable programs.

## 1. Meaning of Object-Oriented Programming

OOP represents a software system using objects that model entities or concepts.

Examples include:

- Student.
- Employee.
- Bank account.
- Vehicle.
- Product.

An object combines information and operations associated with that entity.

## 2. Classes

A class is a blueprint or template used to create objects.

It defines:

- Attributes.
- Methods.
- Initialisation behaviour.
- Relationships with other classes.

Example:

CLASS STUDENT

    ATTRIBUTE NAME
    ATTRIBUTE MARKS

    METHOD DISPLAY()
        OUTPUT NAME
        OUTPUT MARKS
    END METHOD

END CLASS

## 3. Objects

An object is an instance of a class.

If STUDENT is a class, individual students can be represented as separate objects.

Example:

STUDENT1 = Student("Asha", 90)

STUDENT2 = Student("Rahul", 85)

Both objects follow the same class structure but contain different data.

## 4. Attributes and Methods

**Attributes:** Represent the data associated with an object.

Examples:

- Name.
- Age.
- Identification number.
- Account balance.

**Methods:** Represent operations performed by or associated with an object.

Examples:

- Display details.
- Calculate salary.
- Deposit money.
- Withdraw money.

## 5. Constructors

A constructor is a special method or mechanism used to initialise an object when it is created.

Example in Python:

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

The __init__ method initialises the object's attributes in Python.

Constructor syntax differs between languages.

## 6. Four Fundamental OOP Concepts

### Encapsulation

Encapsulation combines data and related methods within a class and controls how internal state is accessed or modified.

It helps protect an object's internal implementation.

### Abstraction

Abstraction hides unnecessary implementation details and exposes essential operations.

For example, a user can operate a car without understanding every internal engine mechanism.

### Inheritance

Inheritance allows one class to derive properties and behaviour from another class.

Example:

Vehicle is a general class.

Car and Motorcycle may be derived classes.

### Polymorphism

Polymorphism allows different objects or classes to respond to the same interface or operation in different ways.

For example, different shapes may implement an AREA method differently.

## 7. Advantages of OOP

- Code reuse.
- Modularity.
- Easier maintenance.
- Improved organisation.
- Better representation of complex entities.
- Extensibility through class relationships.

## 8. Limitations of OOP

- Can introduce unnecessary complexity for simple tasks.
- Poor class design can create tightly coupled systems.
- Excessive inheritance can make software difficult to maintain.
- Object-oriented designs may require additional planning.

## 9. Procedural and Object-Oriented Programming

| Procedural programming | Object-oriented programming |
|---|---|
| Organised around procedures and functions | Organised around objects and classes |
| Focuses on operations | Combines data and behaviour |
| Often uses a top-down design approach | Often models entities and their relationships |
| Example: C | Examples: Java, C++ and Python |

Both approaches can be used to develop effective software.

## Common Exam Traps

- A class is a blueprint for objects.
- An object is an instance of a class.
- Attributes store object-related data.
- Methods define object-related behaviour.
- Encapsulation combines data and behaviour while controlling access.
- Abstraction hides unnecessary implementation details.
- Inheritance supports reuse through class relationships.
- Polymorphism allows different implementations through a common interface.

## Quiz

1. What is a class in object-oriented programming?

- [ ] A physical computer component.
- [ ] A database query.
- [x] A blueprint used to create objects.
- [ ] A type of network cable.

> A class defines the structure and behaviour that its objects can have.

2. Which OOP concept allows a class to derive properties and behaviour from another class?

- [ ] Encapsulation.
- [ ] Abstraction.
- [x] Inheritance.
- [ ] Compilation.

> Inheritance enables a derived class to reuse and extend the features of a base class.

3. Which concept allows different objects to respond differently to the same operation or interface?

- [ ] Data compression.
- [ ] Iteration.
- [ ] Encapsulation.
- [x] Polymorphism.

> Polymorphism allows different implementations to be used through a common interface.