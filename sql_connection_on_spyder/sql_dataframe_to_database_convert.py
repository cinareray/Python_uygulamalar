## 08.11.2020 burda kaldın


import mysql.connector as sql
import numpy as np
import pandas as pd

db = sql.connect(host='localhost', user='root', password = 'mysql1234')
myc = db.cursor()

##                  DATAFRAME'DEN MYSQL database FORMUNA DÖNÜŞTÜRMEK???????

df1= pd.read_sql('''select * from shopapp.python_data''',con = db)
print(df1)

kisiler = pd.DataFrame({'id':(0,1,2),
                        'last_name' : ('mahmut','caner','mehmet'),
                        'first_name':('oturan', 'çoşkun', 'yaren')})
print(kisiler)

#kisiler dataframe database ortamında bir tablo şeklinde kayıt edelim
db_ekleme = sql.connect(host='localhost', user='root', password = 'mysql1234',database= 'shopapp')
kisiler.to_sql(name= 'python_data2', con = db_ekleme,if_exists='append')
