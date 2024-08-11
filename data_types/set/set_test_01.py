
numbers  = [1,2,3,2,2,4,3,3,5,6,6,7]
# print("list:", numbers)

unique_numbers = set(numbers)
# print("set:", unique_numbers)

# unique_numbers.add(10)
# print("set after adding element:", unique_numbers)

# unique_numbers.remove(1)
# print(unique_numbers)

# unique_numbers.pop()
# print(unique_numbers)


names_one = set({'mursalim', 'anu', 'sameer','mursalim'})
names_two = set({'sameer', 'aavesh', 'azibur'})

print(names_two.intersection(names_one))


# print(hash(name))


# name = {'s','a', 'm', 'e', 'e', 'r'}
# print(name)

cities = frozenset({'hyderabad', 'delhi', 'bengaluru', 'pune'})
# for city in cities:
#     print(city, end=',')