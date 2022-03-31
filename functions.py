# following along with this tutorial - https://www.freecodecamp.org/news/connect-python-with-sql/
import mysql.connector
from mysql.connector import Error
import pandas as pd
import queries


# this function (create_server_connection)  is REUSABLE SERVER CONNECTION
# change the argumnts to suit futur projects
from pandas._config import display


def create_db_server_connection(host_name, user_name, user_password, db_name):
    # connection starts as 'none'
    connection = None
    # then connection gets assigned.
    try:
        connection = mysql.connector.connect(
            # input 'root' for user/password/unless you've a specific input
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    # except, if there is an error in connecting, print 'err'
    except Error as err:
        print(f"Error: '{err}'")
    return connection
    # for more info : https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html


# name it
# my username/pssword = root
my_connection = create_db_server_connection("localhost", "root", "root", "school")


# this function (create_database_connection)  is REUSABLE DB CONNECTION
# two arguments - connection and sql query
def create_database(connection, query):
    # cursor - object-orientated method, look up execute and executamy (i think of this like enumaate in py,
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


# call it/name it
# create_database_query = "CREATE DATABASE school"
# create_database(my_connection, create_database_query)

# this is a good time to look at what youre doing/look at ERD

# good idea to automatically connect to right mysql db by default.
# to do this fo to 'create_db_server_connection' and add db_name, in this case 'school'


# this function takes sql queries/py. strings -> passes to cursor/server
# it is same as create_database, but adds connection.commit, which helps user implement queries
# e.g. it lets user creates tables,update, delete, etc with db

# it takes two queries
def execute_query(connection, query):
    # creates a cursor object, so I can inherit child properties/object-orientating
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        # executes in server connection and implements queries
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


# function for reading my db in python
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        # this fetchall lets us get the data into our python
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

#  CRUD create record from list
def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

# ABOVE = all my functions
# BELOW = ALL MY COMMANDS
