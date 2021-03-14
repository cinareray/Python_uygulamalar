import mysql.connector as sql

db = sql.connect(host = 'localhost',
                 user = 'root',
                 password = 'mysql1234',
                 )

mycursor = db.cursor()
mycursor.execute('SHOW DATABASES')
for i in mycursor:
    #print('Database: ' , i)
db = sql.connect(host = 'localhost',
                 user = 'root',
                 password = 'mysql1234',
                 database = 'python_data')    
mycursor = db.cursor()
mycursor.execute('SHOW TABLES')
for a in mycursor:
    print('TABLES', i)