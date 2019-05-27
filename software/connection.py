import pyodbc
server_name =  "LAPTOP-3HO5A040\\SQLEXPRESS" #Insira o seu servido aqui
db_name = "tpc-h"
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server='+server_name+';'
                      'Database='+db_name+';'
                      'Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute("SELECT * from dbo.part")	
