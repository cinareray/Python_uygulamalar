import mysql.connector as sql
db = sql.connect(host='localhost', user='root', password = 'mysql1234')
myc = db.cursor()
myc.execute('select * from shopapp.python_data')

result = myc.fetchall()
print(type(result),'\n')
for i in result:
    print(i)
# columns görüntüleme
myc.execute('select first_name from shopapp.python_data')
result2=myc.fetchall()
for a in result2:
    print(a)
  
#ilk sutunu görmek istersek
myc.execute('select * from shopapp.python_data')
result3 = myc.fetchone()
print(result3)