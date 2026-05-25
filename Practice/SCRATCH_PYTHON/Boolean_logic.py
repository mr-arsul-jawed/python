#Precedence
#Python follows priority order:
""""
()
**
*, /, %
+, -
comparison
not
and
or 
"""

# And operator
age = 20
citizen = True

# print(age >= 18 and citizen)

# Or operator
age = 16
citizen = False
# print(age >= 18 or citizen)

# Not operator
age = 16
# print(not age >= 18)


#Complex Boolean Example
age = 20
has_id = True

# print(age >= 18 and has_id)

# Boolean Precedence
# not , and , or

True or False and False

#Step: First and
#Step: Then or

# Answer: True

#Identity Operators
# is and is not

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

# Membership Operators
# in and not in

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("grape" not in fruits)
