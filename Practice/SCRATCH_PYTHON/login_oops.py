# class
'''
Definition

Blueprint/template.

Example:

House blueprint.

Blueprint not real house.

Only design.

'''
#Python:

class Student:
    def info(self):
        print("Student")

#No real object yet.

#Object

'''
Object = actual thing created.

Example: Blueprint → house.

Class → object.

s1 = Student()

Now object exists.
'''

#internal working :

'''Internal Thinking

Class: template

Object:memory instance

Each object has own memory.

'''
#Example:

'''Example:

class Student:

    def __init__(self,name):
        self.name = name

        
Objects: s1 = Student("Arsul")
s2 = Student("Rahul")

Memory: s1.name → Arsul
s2.name → Rahul

Separate memory.

'''