import trees

myDat,labels = trees.CreateDataSet()
print(myDat)
print(trees.calcShannonEnt(myDat))

myDat[0][-1] = 'maybe'
print(myDat)
print(trees.calcShannonEnt(myDat))