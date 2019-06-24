import os 
import shutil
class Error(Exception): pass

class HashJoin:
  bufferTuple = dict()
  def __init__(self,table1,index1,table2,index2):
    self.table1 = table1
    self.table2 = table2
    self.result = ''

    R = (self.table1[:-4])
    S = (self.table2[:-4])
    self.returnName = "%sJOIN%s.txt" %(R,S)
    """Header in the final result"""
    with open(self.returnName,'w') as w:
      pass

    """Definindo o index"""
    with open(table1,'r') as t1:
      linha1 = t1.readline()
      """Pega as colunas da primeira tabela"""
      self.result += linha1.strip('\n')
      columns = linha1.strip('\n').split(';')
      self.index1 = columns.index(index1)

    with open(table2,'r') as t2:
      linha2 = t2.readline()
      """Concatena as colunas da primeira tabela com as da segunda tabela"""
      self.result += ';'+linha2
      columns = linha2.strip('\n').split(';')
      self.index2 = columns.index(index2)
    """Index estabelecido"""

    self._bucket1 = 'bucket%s' %R
    self._bucket2 = 'bucket%s' %S
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

  """O _loadBucket itera por cada tupla da tabela dada aplica a 
  função hash e adiciona a tupla na página com o id igual ao da função hash"""
  def _loadBucket(self,table,index,bucket,flag):
    with open(table,'r') as table:
      if flag:
        for n,linha in enumerate(table):
          if n>0:
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
      with open(self.returnName ,"a+") as file:
        file.write(str(result))
    except:
      raise Error('Failed while loading the join result to disk')

  def hashjoin(self):

    """Primeira parte do Algoritmo, onde são criados os buckets"""
    self._loadBucket(self.table1,self.index1,self._bucket1,self.flag1)
    self._loadBucket(self.table2,self.index2,self._bucket2,self.flag2)

    R = os.listdir(self._bucket1)
    S = os.listdir(self._bucket2)

    B = dict()

    """Segunda parte do algoritmo, onde se é criado a tabela de índices"""
    for p in  R:
      filename = "%s/%s" %(self._bucket1,p)
      with open(filename,'r') as bucket:
        for posline,line in enumerate(bucket):
          vector = line.split(';')
          i = self._hash(vector[self.index1])
          try:
            B[i].append({"value":vector[self.index1],"pointer":(filename,posline)})
          except:
            B[i] = []
            B[i].append({"value":vector[self.index1],"pointer":(filename,posline)})
    """Aqui é feito o index nested loop join"""

    result = self.result
    counter = 0
    for ps in S:
      with open("%s/%s" % (self._bucket2,ps),"r") as bucket2:
        for l,ts in enumerate(bucket2):
          columns_S = ts.split(";")
          joinAttr_S = columns_S[self.index2] 
          i = self._hash(joinAttr_S)
          if i in B:
            for j in B[i]:
              if(joinAttr_S == j["value"]):
                with open(j["pointer"][0],"r") as bucket1: 
                  for n,tr in enumerate(bucket1):
                    if n == j["pointer"][1]:
                      if (counter > 100000):
                        self._deployResult(result)
                        result = ''
                        counter = 0
                      result += tr.strip("\n") + ';' + ts
                      counter += 1                       
    self._deployResult(result)

    #shutil.rmtree(self._bucket1, ignore_errors=True)
    #shutil.rmtree(self._bucket2, ignore_errors=True)
    return self.returnName
              
if __name__ == "__main__":
    import time
    
    h = HashJoin("partsupp.txt",'ps_suppkey',"part.txt","p_partkey")
    begin = time.time()
    print(h.hashjoin())
    end = time.time()
    print("Execution time:",(end-begin))

