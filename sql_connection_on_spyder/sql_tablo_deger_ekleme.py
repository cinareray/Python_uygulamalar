## oluşturulan python_data database python_data tablosuna ekleme yapalım

import mysql.connector as sql
db = sql.connect(host='localhost', user='root', password = 'mysql1234',
                 database= 'shopapp')
myc = db.cursor()
a = ('insert into python_data (last_name,first_name) values (%s,%s)')
b = ('mutlu', 'kolcu')
myc.execute(a,b)


db.commit()
print("1 record inserted, ID:", myc.lastrowid)