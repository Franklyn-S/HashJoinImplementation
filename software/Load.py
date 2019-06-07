import pyodbc
class Load:
	def __init__(self, server,db,user,passw,):
		self.server = server
		self.db = db
		self.user = user
		self.passw = passw		
	def load(self,table):
		cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server='+self.server+';'
                      'Database='+self.db+';'
                      'UID='+self.user+';'
					  'PWD='+self.passw+';'
                      'Trusted_Connection=yes;')

		query = "Select * from %s" %table
		cursor = cnxn.cursor()
		cursor.execute(query)

		filename = '%s.txt' %table
		file = open(filename, 'w')
		tupla = cursor.description
		colunas = []
		for i in tupla:
			colunas.append(i[0])
		for linha in cursor:
		    string = ""
		    for index in range(0,len(colunas)):
		    	if index == len(colunas) - 1:
		    		string += str(linha[index])
		    	else:
		        	string += str(linha[index])+","
			
		    file.write(string+"\n")
		file.close()
		cursor.close()
		return filename

if __name__ == "__main__":
	loader = Load("LAPTOP-3HO5A040\\SQLEXPRESS","tpc-h",'','')
	print(loader.load("part"))