import os 

class Error(Exception): pass

class HashJoin:
  bufferTuple = dict()
  def __init__(self,table1,index1,table2,index2):
    self.table1 = table1
    self.table2 = table2

    #Definindo o index
    with open(table1,'r') as t1:
      linha1 = t1.readlines()
      columns = linha1[0].strip('\n').split(';')
      self.index1 = columns.index(index1)

    with open(table2,'r') as t2:
      linha2 = t2.readlines()
      columns = linha2[0].strip('\n').split(';')
      print(columns)
      self.index2 = columns.index(index2)
    #Index estabelecido

    self._bucket1 = 'bucket%s1' %(table1[:-4].upper())
    self._bucket2 = 'bucket%s2' %(table2[:-4].upper())
    self.flag1 = False
    self.flag2 = False

    self.watcher = 0
    
    if not os.path.isdir(self._bucket1):
      os.mkdir(self._bucket1)
      self.flag1 = True
    if not os.path.isdir(self._bucket2):
      os.mkdir(self._bucket2)
      self.flag2 = True

  def _hash(self,index):
    try:
      index = int(index)
      return ((23*index+20)%1000)%97
    except:
      return hash(index)

  def _deployDict(self,bucket):
    try:
      for key in self.bufferTuple:
        with open("%s/%s.txt" %(bucket,key),"a+") as file:
          file.write(str(self.bufferTuple[key]))
      self.bufferTuple = dict()
    except:
      raise Error("File failed while load the bucket to the disk")

  #O _loadBucket itera por cada tupla da tabela dada aplica a 
  #função hash e adiciona a tupla na página com o id igual ao da função hash
  def _loadBucket(self,table,index,bucket,flag):
    with open(table,'r') as table:
      linhas = table.readlines()

      if not flag:
        raise Error("Error: Buckets with this name already exists")
      for linha in linhas[1:]:
        vetorLinha = linha.split(";")
        id = self._hash(vetorLinha[index])
        if self.watcher < 100000:
          try:
            self.bufferTuple[id] += linha
          except:
            self.bufferTuple[id] = ''
            self.bufferTuple[id] += linha
          finally:
            self.watcher += 1
        else:
          self._deployDict(bucket)

      self._deployDict(bucket)




  def hashjoin(self):
    self._loadBucket(self.table1,self.index1,self._bucket1,self.flag1)
    self._loadBucket(self.table2,self.index2,self._bucket2,self.flag2)

    R = os.listdir(self._bucket1)
    S = os.listdir(self._bucket2)

    
        


if __name__ == "__main__":
    import time
    
    h = HashJoin("nation.txt",'n_nationkey',"part.txt",'p_partkey')
    begin = time.time()
    print(h.hashjoin())
    end = time.time()
    print("Execution time:",(end-begin))

