# we can define a function with def keyword and ident should be 1 tab space or 4 spaces for better practice
# a function can have any no of arguments
# a function can return a value
# we can call a function inside another function
# Execution always begins at the first statement of the program. Statements are executed one at a time, 
# in order from top to bottom.
# function which not return a value called a void function




def findSum(a,b):
 return a+b

sum =findSum(10,20)

print( "sum of two numbers is: ", sum)


# check if a number given is even or odd 

def    checkEvenOdd(a):
 if(a%2==0):  print("number is even")
 else: print("number is odd")

checkEvenOdd(20)
checkEvenOdd(55)
checkEvenOdd(13)

