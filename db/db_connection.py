import mysql.connector as connector 

# Connect with db
try:
    connection = connector.connect(user='root',database="python_test_db",password='root', host='127.0.0.1') 
    cursor = connection.cursor()
    create_table = '''  create table if not exists 
        users(user_id int(10), user_name varchar(20), user_department varchar(20)) 
        '''
    cursor.execute(create_table)
    
except connector.DatabaseError as dbe:
    print(dbe)
else:
    print("user table created.")

finally:
    connection.close()    