# find the element in list using for loop

def search_element_one(list, target):
    for num in range(0, len(list)+1):
        if num == target:
            return "Found element"
    return "Not found the element"    


def search_element_two(list, target):
    if list == None:
        return -1
    if target in list:
        index = list.index(target)
        return index 
    return -1    


list =[1,55,3,2,5,7,43,5,8,6,5,10]

target =99
ans_one =search_element_one(list, target)
print(ans_one)

ans_two =search_element_two(list, target)
print("found element at index", ans_two)