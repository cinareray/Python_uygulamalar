import mysql.connector as sql

db = sql.connect(host = 'localhost',
                 user = 'root', 
                 password = 'mysql1234')

myc = db.cursor()
myc.execute('CREATE DATABASE deneme')