import trees

myDat,labels = trees.CreateDataSet()
# 测试计算香农熵
# print(myDat)
# print(trees.calcShannonEnt(myDat))

# 特征值的增加会使香农熵增加
# myDat[0][-1] = 'maybe'
#print(myDat)
# print(trees.calcShannonEnt(myDat))

# 三个参数 数据集 要划分的特征 特征值
# 在数据集中找特征等于特征值的项
print(trees.splitDataSet(myDat,0,1))