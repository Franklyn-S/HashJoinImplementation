if __name__ == "__main__":
    import time
    
    
    n = int(input("Digite o número de tabelas:"))

    table_list = []
    attribute_list = []
    i = 0
    
    begin = time.time()
        
    while i < n:
        table = str(input('Digite as tabelas:'))
        table_list.append(table)
        i = i + 1

    j = 0
    
    while j < n:
        attribute = str(input('Digite os atributos de junção:'))
        attribute_list.append(attribute)
        j = j + 1

    if(n < 2):
        print("Não é necessária a junção!\n") 

    if(n == 2):
        join = HashJoin(table_list[0],attribute_list[0],table_list[1],attribute_list[1])
        join.hashjoin()
    
    
    if(n == 3): 
            join1 = HashJoin(table_list[0],attribute_list[0],table_list[1],attribute_list[1])
            join2 = join1.hashjoin()
            join3 = HashJoin(join2,attribute_list[0],table_list[2],attribute_list[2])
            join3.hashjoin()
    
    end = time.time()
    
print("Execution time:",(end-begin))