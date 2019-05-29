class HashJoin:
  bucketDict1 = dict()
  bucketDict2 = dict()
  def __init__(self,table1,index1,table2,index2):
    self.table1 = table1
    self.table2 = table2
    self.index1 = index1
    self.index2 = index2

  def hashFunc(self,key):
    return ((23*key+20)%10)%97
    
  def loadBuckets(self):
    for i in self.table1:
      id = hashFunc(self.table1[index1])
      if id not in bucketDict1:
        bucketDict1[id] = []
      else:
        bucketDict1[id].append(i)

    for j in self.table2:
      id = hashFunc(self.table2[index2])
      if id not in bucketDict2:
        bucketDict2[id] = []
      else:
        bucketDict2[id].append(i)

