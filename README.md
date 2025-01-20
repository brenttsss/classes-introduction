# Classes Introduction - README

What are objects?

An object is a container for variables and functions.
A monster object might contain:
Variables for health, energy, stamina and damage.
Functions for attack, movement and animations.

Variables and functions exist in the object container.
Variables are called attributes, while functions are called methods.

It is possible to have multiple objects with their own attributes and methods.

What is object-oriented programming?

Code is organised via objects and almost all large projects are organised like this.
Objects can interact with each other.

What are classes?
A class is the blueprint for an object. A class can also inherit from another class.

Why use classes and objects?

They organise complex code.
They help to create reusable code.
They are used everywhere.
Some modules require you to crease classes (eg. pygame, tkinter, and matplotlib).
They make it easier to work with scope.

What is the dunder (double underscore) method?

A dunder method is a method that is not called by the user. Instead, it is called by python when something happens
__init__ is called when the object is created
__len__ is called when the object is passed into len()

A function and a method both execute a block of code. The difference is that a method belongs to an object.

Since every method has a reference to the class, it is easy to get and change class attributes. Hence, methods rely much less on parameters, global and return.

Inheritance means that one class gets attributes and methods from another class or classes.
This makes it easier to reuse code. We can have a parent and child class, then combine them to form an object.
A class can inherit from an unlimited number of other classes. A class can also be inherited from by an unlimited number of classes.
Inheritance can get very complex :(