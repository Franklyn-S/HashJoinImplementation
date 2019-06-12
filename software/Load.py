import pyodbc
import time

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

		strColunas = ''
		counter = 0 
		for i in tupla:
			if counter == len(tupla) - 1:
				strColunas += str(i[0])
			else:
				strColunas += str(i[0]+';')
			counter += 1

		file.write(strColunas+"\n")

		string = ""
		tuplecounter = 0 
		for linha in cursor:
		    for index in range(0,counter):
		    	if index == counter - 1:
		    		string += str(linha[index])
		    	else:
		        	string += str(linha[index])+";"
		    string += '\n'
		    if tuplecounter>100000:
		        file.write(string)
		        string = ''
		    tuplecounter += 1
		file.write(string)
		file.close()
		cursor.close()
		return filename

if __name__ == "__main__":
	loader = Load("LAPTOP-3HO5A040\\SQLEXPRESS","tpc-h",'','')
	begin = time.time()
	print(loader.load("part"))
	end = time.time()
	print("Execution time:",(end-begin))