import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user='root', password = 'mysql1234')

print(mydb)

if (mydb):
    print("Connection Succesfull")
    
    