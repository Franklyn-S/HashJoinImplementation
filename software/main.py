if __name__ == "__main__":
    import time
    from HashJoin import HashJoin
    
    
    n = int(input("Digite o número de tabelas:"))

    table_list = []
    attribute_list = []
    i = 0
    
    begin = time.time()

    print("Insira o nome da tabela junto do atributo de junção da seguinte forma: 'tabela','atributo'")
    while i < n:
        table = str(input('Insira os dados:'))
        table = table.split(',')
        table_list.append((table[0]+'.txt',table[1]))
        i = i + 1


    if(n < 2):
        print("Não é necessária a junção!\n") 

    if(n == 2):
        print(table_list[0][0],table_list[0][1],table_list[1][0],table_list[1][1])
        join = HashJoin(table_list[0][0],table_list[0][1],table_list[1][0],table_list[1][1])
        join.hashjoin()
    
    
    if(n == 3): 
        print(table_list[0][0],table_list[0][1],table_list[1][0],table_list[1][1])
        join1 = HashJoin(table_list[0][0],table_list[0][1],table_list[1][0],table_list[1][1])
        join2 = join1.hashjoin()
        print(join2,table_list[0][1],table_list[2][0],table_list[2][1])
        join3 = HashJoin(join2,table_list[0][1],table_list[2][0],table_list[2][1])
        join3.hashjoin()
    
    end = time.time()
    
print("Execution time:",(end-begin))