import mysql.connector as connector 

# Connect with db
connection = connector.connect(user='root', password='root', host='localhost') 

cursor = connection.cursor()

# show all databases query
show_dbs= "SHOW DATABASES"

with connection.cursor() as cursor:
    cursor.execute(show_dbs)
    for db in cursor:
        print(db)


# connect to existing db
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="test_db",
    ) as connection:
        print(connection)
except Error as e:
    print(e)




