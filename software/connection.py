import pyodbc
server_name =  "200.19.182.252" #Insira o seu servido aqui
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
#cursor.execute("SELECT * from dbo.part")	

