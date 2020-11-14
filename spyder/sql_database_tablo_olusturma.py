import mysql.connector as sql

db = sql.connect(host = 'localhost',
                 user = 'root',
                 password = 'mysql1234',
                 database = 'shopapp')

mycursor = db.cursor()
mycursor.execute('CREATE TABLE python_data (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, last_name  VARCHAR(45), first_name VARCHAR(45))')
