import os 

class HashJoin:

  def __init__(self,table1,index1,table2,index2):
    self.table1 = open(table1,'r') 
    self.table2 = open(table2,'r')
    self.index1 = index1
    self.index2 = index2
    self._bucket1 = 'bucket%s1' %(table1[:-4].upper())
    self._bucket2 = 'bucket%s2' %(table2[:-4].upper())
    self.flag = False
    try:
      os.mkdir(self._bucket1)
      os.mkdir(self._bucket2)
      self.flag = True
    except:
      pass

  def _hash(self,index):
    try:
      index = int(index)
      return hash(index)
    except:
      return hash(index)

  #O _loadBucket itera por cada tupla da tabela dada aplica a 
  #função hash e adiciona a tupla na página com o id igual ao da função hash
  def _loadBucket(self,table,index,bucket):
    linhas = table.readlines()
    if not self.flag:
      return "Error: Cannot loadBuckets"
    for linha in linhas:
      vetorLinha = linha.split(",")
      id = self._hash(vetorLinha[index])
      try:
        bucketfile = open("%s/%s.txt" %(bucket,id),"r")
      except:
        bucketfile = open("%s/%s.txt" %(bucket,id),"w")
        bucketfile.close()

        bucketfile = open("%s/%s.txt" %(bucket,id),"r")
      finally:
        content = bucketfile.readlines()

        content.append(linha)
        bucketfile = open("%s/%s.txt" %(bucket,id),"w")
        for line in content:
          bucketfile.write(line)
        bucketfile.close()

  def hashjoin(self):
    self._loadBucket(self.table1,self.index1,self._bucket1)
    self._loadBucket(self.table2,self.index2,self._bucket2)
        


if __name__ == "__main__":
    import time
    
    h = HashJoin("nation.txt",0,"nation.txt",0)
    begin = time.time()
    print(h.hashjoin())
    end = time.time()
    print("Exeecution time:",(end-begin))

