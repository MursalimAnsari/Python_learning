
#Fundamental data types vs Immutability

"""
If we are creating a new object in python then PVM won't create object directly into the memory
first it will check if any object is present in heap or not,
if there is any object in memory then PVM will create a reference to that object,
Otherwise PVM create new object in Heap and create reference to that object...

If multiple variables refer to a single object in heap and if someone tries to change the value 
then PVM will not change that object instead it will create a new object and create reference link
to that variable.
It is to ensure immutability as once we create an object then it's value can't be changed.

All objects in python are immutable.

Advantage :
Better memory utilisation
Performance will be increased
"""

# Why reusability concept is there in python: 
"""
  suppose we have to create objects in python then at the time of interpreter start
  python virtual machine will create the objects for int, float, str,and boolean
  why???
  To increase the performance at run time

   How it will check that system is going to create an object at the start of interpreter:
   for int : 0-256 objects created
   bool : always created
   str: always

"""

a = 20 
print("unique identifier before changing object for a",id(a))
b=20 
c= 20

# a= 40

# print("unique identifier after chaning object for a", id(a))
# print("unique identifier for b", id(b))
# print('unique identifier for b',id(c))

# is operator is used to check if both objects have same unique id 

print(a is b)
print(a is c)
print(b is c)




