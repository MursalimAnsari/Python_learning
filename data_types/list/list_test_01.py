
# numbers = [1,2,32,3,2,2,4,4,5,56,67,67,6,]
# print(numbers)

# # methods 
# # append number at end 
# # numbers.append(200)
# # print(numbers)

# # sort
# # numbers.sort()
# # print(numbers)



# # numbers_1 = numbers.copy()

# # print(id(numbers_1))
# # print(id(numbers))


# """
# Shallow copy: a new object created with the refernces of the original object
#               it does not copy the nesed objects


# Deep copy: creates a new object containing the ll objects into the copied object
#            it copies the nested objects into the copied object
# """


# original_list = [10,20,30]
# copied_list   = original_list.copy()

# copied_list.append(50)

# print(original_list)
# print(copied_list)


# Shallow copy

# original_list_obj = [[10,20],[50],[80,90]]
# copied_list_obj   = original_list_obj.copy()

# copied_list_obj[0].append(35)

# print(original_list_obj)
# print(copied_list_obj)


import copy


original_list_obj = [[10,20],[50],[80,90]]
copied_list_obj   = copy.deepcopy(original_list_obj)

copied_list_obj[0].append(35)

print(original_list_obj)
print(copied_list_obj)
