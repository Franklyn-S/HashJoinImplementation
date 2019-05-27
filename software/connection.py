import pyodbc
server_name =  "LAPTOP-3HO5A040\\SQLEXPRESS"
db_name = "tpc-h"
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server='+server_name+';'
                      'Database='+db_name+';'
                      'Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute("SELECT * from dbo.nation")	

arq = open('nation.txt', 'w')
tupla = cursor.description
colunas = []
for i in tupla:
	colunas.append(i[0])
for linha in cursor:
    string = ""
    for index in range(0,len(colunas)):
        string += str(linha[index])+","
	
    arq.write(string+"\n")
arq.close()
cursor.close()
