PATH_FILE = "d:/@home_personal/projects_2024/Python_learning/file_handling/abc.txt"

print("Reading file data ")

try:
    print("open file")
    with open(PATH_FILE, "r") as file:
     data = file.read()
     print(data)
except FileNotFoundError as err:
    print("file doesn't exist: ", err)
finally:
    print("closing the file")
    file.close()    
    print("closed the file object")    