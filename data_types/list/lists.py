
"""
    A built in data type in python that stores set of values
    it can store elements of different types [1,3,"abc", 6.7] e.t.c , i.e. heterogenous elements allowed
    it is an ordered collection, insertion order preserved
    can contain duplicate values
    mutable i.e. once created it can be modified
    growable in size
    values should be enclosed within square bracket
"""

numbers = [1,2,3,22,45,4,5,6,6]

# print(type(numbers), numbers)
# print("length of list: ", len(numbers))

# numbers.append(70)
# print("count of 6 is: ", numbers.count(6))
# print("index of 6 is: ", numbers.index(6))
# print(numbers)

# remove the last element from the list
# print("last element popped is: ", numbers.pop())
# print("numbers list after the pop: ", numbers)


# reverse the list elements
# numbers.reverse()
# print(numbers)

# sort the list in descending order
# numbers.sort(reverse=True)
# print("sorted list: ", numbers)

# sort the list in ascending order
# numbers.sort()
# print("sorted list: ", numbers)

#=============================================#
# list.copy() method is used to create a copy of original list
# If we change or alter the copy list it won't affect the original list 

# copyList = numbers.copy()
# print("copy list before append element: " ,copyList)
# copyList.append(90)
# print("copy list after append element: " ,copyList)
# print("original list after append in copy list: ", numbers)

