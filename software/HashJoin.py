class HashJoin:
  bucketDict1 = dict()
  bucketDict2 = dict()
  def __init__(self,table1,index1,table2,index2):
    self.table1 = open(table1,'r')
    self.table2 = open(table2,'r')
    self.index1 = index1
    self.index2 = index2

  def _hash(self,index):
    try:
      index = int(index)
      print(type(index))
      return hash(index)
    except:
      print(type(index))
      return hash(index)

  def loadBuckets(self):
    linhas = self.table1.readlines()
    for linha in linhas:
      vetorLinha = linha.split(",")
      id = self._hash(vetorLinha[self.index1])
      if id not in self.bucketDict1:
        self.bucketDict1[id] = []
        self.bucketDict1[id].append(linha)
      else:
        self.bucketDict1[id].append(linha)

    linhas = self.table2.readlines()
    for linha in linhas:
      vetorLinha = linha.split(",")
      id = self._hash(vetorLinha[self.index2])
      if id not in self.bucketDict2:
        self.bucketDict2[id] = []
        self.bucketDict2[id].append(linha)
      else:
        self.bucketDict2[id].append(linha)

    print(self.bucketDict1,"\n\n\n",self.bucketDict2)

if __name__ == "__main__":
    h = HashJoin("nation.txt",0,"nation.txt",0)
    h.loadBuckets()

