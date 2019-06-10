import pyodbc
server_name =  "LAPTOP-3HO5A040\\SQLEXPRESS"
db_name = "tpc-h"
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server='+server_name+';'
                      'Database='+db_name+';'
                      'UID=;'
                      'PWD=;'
                      'Trusted_Connection=yes;')



cursor1 = cnxn.cursor()
cursor2 = cnxn.cursor()
cursor3 = cnxn.cursor()

query1 = "SELECT * from %s" %("TPCSOURCE.NATION")
cursor1.execute(query1)

arq1 = open('nation.txt', 'w')
tupla1 = cursor1.description
colunas1 = []
for i in tupla1:
  colunas1.append(i[0])
for linha1 in cursor1:
    string1 = ""
    for index in range(0,len(colunas1)):
        string1 += str(linha1[index])+";"
  
    arq1.write(string1+"\n")
arq1.close()
cursor1.close()



query2 = "SELECT * from  %s" %("TPCSOURCE.SUPPLIER")
cursor2.execute(query2)
arq2 = open('supplier.txt', 'w')
tupla2 = cursor2.description
colunas2 = []
for j in tupla2:
  colunas2.append(j[0])
for linha2 in cursor2:
    string2 = ""
    for index2 in range(0,len(colunas2)):
        string2 += str(linha2[index2])+";"
  
    arq2.write(string2+"\n")
arq2.close()
cursor2.close()


query3 = "SELECT * from  %s" %("TPCSOURCE.PARTSUPP")
cursor3.execute(query3)
arq3 = open('partsupp.txt', 'w')
tupla3 = cursor3.description
colunas3 = []
for k in tupla3:
  colunas3.append(k[0])
for linha3 in cursor3:
    string3 = ""
    for index3 in range(0,len(colunas3)):
        string3 += str(linha3[index3])+";"
  
    arq3.write(string3+"\n")



arq3.close()
cursor3.close()


