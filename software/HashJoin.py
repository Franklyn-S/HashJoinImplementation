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
      raise Error("File failed while loading the bucket to the disk")

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
        if self.watcher > 100000:
          self._deployDict(bucket)
          self.watcher = 0
        try:
          self.bufferTuple[id] += linha
        except:
          self.bufferTuple[id] = ''
          self.bufferTuple[id] += linha
        finally:
          self.watcher += 1          

      self._deployDict(bucket)


  def _deployResult(self, result):
    try:
      with open("Result.txt" ,"a+") as file:
        file.write(str(result))
    except:
      raise Error('Failed while loading the join result to disk')




  def hashjoin(self):
    self._loadBucket(self.table1,self.index1,self._bucket1,self.flag1)
    self._loadBucket(self.table2,self.index2,self._bucket2,self.flag2)

    R = os.listdir(self._bucket1)
    S = os.listdir(self._bucket2)
    print(R,"\n",S)


    result = ''
    counter = 0

    for ps in S:
        with open("%s/%s" % (self._bucket2,ps),"r") as bucket2:
          lines_S = bucket2.readlines()
          for ts in lines_S:
            columns_S = ts.split(";")
            joinAttr_S = columns_S[self.index2] 
            i = self._hash(joinAttr_S)
            if ("%s.txt" %i) in R:
              with open("%s/%s.txt" % (self._bucket1,i),"r") as bucket1:
                lines_R = bucket1.readlines()
                for tr in lines_R:
                  columns_R = tr.split(";")
                  joinAttr_R = columns_R[self.index1]
                  if(joinAttr_R == joinAttr_S):
                    if (counter < 100000):
                      result += tr + ';' + ts + '\n'
                      counter += 1  
                    else:
                      result += tr + ';' + ts + '\n'
                      self._deployResult(result)
                      result = ''
    self._deployResult(result)
              
if __name__ == "__main__":
    import time
    
    h = HashJoin("part.txt",'p_partkey',"nation.txt",'n_nationkey')
    begin = time.time()
    print(h.hashjoin())
    end = time.time()
    print("Execution time:",(end-begin))

