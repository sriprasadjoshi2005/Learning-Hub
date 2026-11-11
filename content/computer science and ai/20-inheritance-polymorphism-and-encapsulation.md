---
title: Inheritance, Polymorphism and Encapsulation
level: intermediate
---

Inheritance, polymorphism and encapsulation are three fundamental concepts of object-oriented programming. They support code reuse, controlled access to data and flexible software design.

## 1. Inheritance

Inheritance allows a new class to acquire attributes and methods from an existing class.

The existing class is commonly called the:

- Parent class.
- Base class.
- Superclass.

The new class is commonly called the:

- Child class.
- Derived class.
- Subclass.

Example:

CLASS ANIMAL
    METHOD EAT()
        OUTPUT "Eating"
    END METHOD
END CLASS

CLASS DOG EXTENDS ANIMAL
    METHOD BARK()
        OUTPUT "Barking"
    END METHOD
END CLASS

An object of DOG can use its own BARK method and inherit the EAT method from ANIMAL.

## 2. Types of Inheritance

### Single Inheritance

One child class inherits from one parent class.

### Multilevel Inheritance

A class inherits from another derived class.

Example:

ANIMAL -> MAMMAL -> DOG

### Hierarchical Inheritance

Multiple child classes inherit from the same parent class.

Example:

ANIMAL -> DOG

ANIMAL -> CAT

### Multiple Inheritance

A class inherits from more than one parent class.

Example:

CLASS CHILD EXTENDS PARENT1, PARENT2

Not all programming languages support multiple class inheritance.

### Hybrid Inheritance

A combination of different inheritance patterns.

The availability and implementation of these inheritance forms depend on the programming language.

## 3. Polymorphism

Polymorphism means the ability of different objects or operations to exhibit different behaviours through a common interface or name.

### Compile-Time Polymorphism

In languages that support it, compile-time polymorphism may be achieved through:

- Function overloading.
- Operator overloading.

### Runtime Polymorphism

Runtime polymorphism commonly involves method overriding and dynamic method dispatch.

Example:

CLASS ANIMAL
    METHOD SOUND()
        OUTPUT "Animal sound"
    END METHOD
END CLASS

CLASS DOG EXTENDS ANIMAL
    METHOD SOUND()
        OUTPUT "Bark"
    END METHOD
END CLASS

CLASS CAT EXTENDS ANIMAL
    METHOD SOUND()
        OUTPUT "Meow"
    END METHOD
END CLASS

The same SOUND method produces different results depending on the object's actual type.

## 4. Method Overloading

Method overloading allows multiple methods to share the same name while accepting different parameter lists.

Example:

ADD(A, B)

ADD(A, B, C)

Language support differs. Python does not support traditional method overloading in the same way as languages such as C++ and Java, although similar behaviour can be achieved through flexible parameters or other techniques.

## 5. Method Overriding

Method overriding occurs when a derived class provides its own implementation of an inherited method.

Example:

A parent class defines DISPLAY().

A child class redefines DISPLAY() to provide specialised behaviour.

Overriding is an important mechanism for runtime polymorphism.

## 6. Encapsulation

Encapsulation combines data and the methods that operate on that data within a class.

It also controls access to internal state.

Common access concepts include:

- Public: Accessible through the class's public interface.
- Protected: Intended for use within a class and related subclasses, with language-specific rules.
- Private: Restricted according to the language's access-control mechanisms.

Python uses conventions and name mangling rather than strict private access modifiers in the same way as some other languages.

## 7. Data Hiding

Data hiding restricts direct access to internal implementation details.

Example:

A bank account class may prevent direct modification of its balance and instead provide methods such as:

DEPOSIT(amount)

WITHDRAW(amount)

This allows validation rules to be applied before the balance changes.

## 8. Abstraction and Encapsulation

| Abstraction | Encapsulation |
|---|---|
| Hides unnecessary implementation details | Organises data and behaviour and controls access |
| Focuses on what an object exposes | Focuses on how internal state is protected and managed |
| Simplifies interaction | Helps maintain data integrity |

The concepts are related but not identical.

## 9. Advantages of These Concepts

- Inheritance reduces code duplication.
- Polymorphism supports flexible interfaces.
- Encapsulation protects internal state.
- Method overriding allows specialised behaviour.
- Access control supports better software organisation.
- Well-designed class hierarchies improve maintainability.

## 10. Potential Design Problems

- Deep inheritance hierarchies can become difficult to understand.
- Multiple inheritance can introduce ambiguity.
- Excessive data hiding can make interfaces inconvenient.
- Poorly designed base classes can restrict derived classes.
- Overuse of inheritance can create tight coupling.

Composition is often an alternative to inheritance when a class needs to use the functionality of another class without becoming its subtype.

## Common Exam Traps

- Inheritance represents an IS-A relationship.
- Composition commonly represents a HAS-A relationship.
- Overloading and overriding are different.
- Overloading uses different parameter lists where supported.
- Overriding changes an inherited method's implementation.
- Encapsulation combines data and related methods.
- Data hiding restricts access to internal state.
- Runtime polymorphism commonly uses dynamic method dispatch.

## Quiz

1. Which type of inheritance involves a class deriving from an already derived class?

- [ ] Single inheritance.
- [ ] Hierarchical inheritance.
- [x] Multilevel inheritance.
- [ ] Multiple inheritance.

> Multilevel inheritance creates a chain of classes in which one derived class becomes the base of another.

2. Which concept allows a derived class to provide its own implementation of an inherited method?

- [ ] Method overloading.
- [ ] Encapsulation.
- [x] Method overriding.
- [ ] Data abstraction.

> Method overriding replaces or specialises an inherited method implementation in a derived class.

3. What is the main purpose of encapsulation?

- [ ] To convert source code into machine code.
- [ ] To execute loops repeatedly.
- [x] To combine data and related behaviour while controlling access to internal state.
- [ ] To store every program in a database.

> Encapsulation organises object data and methods and provides controlled access to internal state.