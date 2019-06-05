import pyodbc
server_name =  "LAPTOP-3HO5A040\\SQLEXPRESS"
db_name = "tpc-h"
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server='+server_name+';'
                      'Database='+db_name+';'
                      'UID=;'
                      'PWD=;'
                      'Trusted_Connection=yes;')
cursor = cnxn.cursor()
query = "SELECT * from %s" %("nation")
cursor.execute(query)

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
#cursor.execute("SELECT * from dbo.part")	

