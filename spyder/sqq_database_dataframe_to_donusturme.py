import mysql.connector as sql
import numpy as np
import pandas as pd

db = sql.connect(host='localhost', user='root', password = 'mysql1234')
myc = db.cursor()
myc.execute('select * from shopapp.python_data')

result = myc.fetchall()
print(type(result),'\n')
a = np.array(result)

df= pd.DataFrame(a)
print(df)
df = df.loc[:,'1':'2']
print(df)
df.columns = ['first_name', 'last_name']
print(df)

##        KISA YOLU

import pandas as pd
import mysql.connector as sql

db = sql.connect(host = 'localhost', 
                user = 'root',
                password ='mysql1234',
                database=  'shopapp')

dff = pd.read_sql("""
select * from python_data""",con=db)
print(dff)

##reference = https://towardsdatascience.com/how-to-convert-sql-query-results-to-a-pandas-dataframe-a50f0d920384