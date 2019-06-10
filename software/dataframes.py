table1 = pd.read_csv('nation.txt',header = None, error_bad_lines=False, sep = ';') #carrega o .txt da tabela nation

col = table1[4]

table1 = table1.drop(columns = [4],axis = 1) #criar o dataframe gera uma coluna aleat�ria no final da tabela, ent�o a apagamos

table1.columns = ['n_nationkey','n_name','n_regionkey','n_comment'] #nomeando as colunas da tabela nation

table2 = pd.read_csv('supplier.txt',header = None, error_bad_lines=False, sep = ';') #carrega o .txt da tabela supplier

table2 = table2.drop(columns = [7],axis = 1) #criar o dataframe gera uma coluna aleat�ria no final da tabela, ent�o a apagamos

table2.columns = ['s_suppkey','s_name','s_address','s_nationkey','s_phone','s_acctbal','s_comment']  #nomeando as colunas da tabela supplier

table3 = pd.read_csv('partsupp.txt',header = None, error_bad_lines=False, sep = ';') #carrega o .txt da tabela partsupp

table3 = table3.drop(columns = [5],axis = 1) #criar o dataframe gera uma coluna aleat�ria no final da tabela, ent�o a apagamos

table3.columns = ['ps_partkey','ps_suppkey','ps_availqty','ps_supplycost','ps_comment']  #nomeando as colunas da tabela partsupp

#salvando as altera��es para o .txt das tabelas

#Sugest�o: os atributos de jun��o poderiam ser: 
# jun��o1: (n_nationkey,s_nationkey)
#jun��o2: (jun��o1['s_suppkey],ps_suppkey)

table1file = open('table1.txt', 'a') #salvando as altera��es para o .txt das tabelas 
table1file.write(table1.to_string())
table1file.close()

table2file = open('table2.txt', 'a')
table2file.write(table2.to_string())
table2file.close()

table3file = open('table3.txt', 'a')
table3file.write(table3.to_string())
table3file.close()

