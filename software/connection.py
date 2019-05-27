import pyodbc
server_name =  "LAPTOP-3HO5A040\\SQLEXPRESS"
db_name = "tpc-h"
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server='+server_name+';'
                      'Database='+db_name+';'
                      'Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute("SELECT * from dbo.part")	

for i in cursor:
	print(i)