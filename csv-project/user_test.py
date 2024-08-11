import os
import csv


def read_data_from_csv_file(file_path):
     
    if not os.path.isfile(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return
    
    try:
        
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  
            data = [row for row in csv_reader]  

            print("Headers:", headers)
            print("Data:", data)

            return headers, data
            
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except csv.Error as e:
        print(f"Error: An issue occurred while reading the CSV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def write_data_to_csv_file(file_path, headers, data):
    try: 
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            
            csv_writer = csv.writer(file)
            csv_writer.writerow(headers)
            csv_writer.writerows(data)

        print(f"Data successfully written to {file_path}")

    except IOError as e:
        print(f"Error: An issue occurred while writing to the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




user_file_path = "d:/@home_personal/projects_2024/Python_learning/csv-project/user.csv"

read_data_from_csv_file(user_file_path)

headers = ['user_id','user_name','salary','department_name']
data = [
   ['6', 'Lucas Gray', '75000.00', 'IT'],
    ['7', 'Alice Green', '69000.00', 'Operations'],
    ['8', 'David Lee', '72000.00', 'Logistics'],
    ['9', 'Olivia Martinez', '65000.00', 'Design'],
    ['10', 'James Wilson', '56000.00', 'Legal']
]

write_data_to_csv_file(user_file_path,headers,data)
print("after adding the data: ")
read_data_from_csv_file(user_file_path)