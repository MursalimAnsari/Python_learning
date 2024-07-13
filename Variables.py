x= 200

# print(x)

y = x 

# verify that two variables having same reference

print("id of x is: ", id(x))
print("id of y is: ", id(y))

#  we have both the id's same hence these both variables are referring to same object
#  id of x is:  140713429525144
# id of y is:  140713429525144 

y=300

print("=======================")
print("id of x is: ", id(x))
print("id of y is: ", id(y))


#  Object life cycle in python: An object's lifecycle begins with creating any object. 
#  It should have at least one reference at a time, As reerence count becomes zero the object will be no
#  longer accessible and it becomes orphan. python will eventually notice it is no longer accessible hence it
#  will be available for garbage collection.
#  The built in function id() returns the unique id of an object
#  if two object have same id then they will return same code 
#  python uses caching for storing the values in range [-5, 256] and it reuses them as needed.