import trees
import treePlotter

myDat,labels = trees.CreateDataSet()
# 测试计算香农熵
# print(myDat)
# print(trees.calcShannonEnt(myDat))

# 特征值的增加会使香农熵增加
# myDat[0][-1] = 'maybe'
# print(myDat)
# print(trees.calcShannonEnt(myDat))

# 三个参数 数据集 要划分的特征 特征值
# 在数据集中找特征等于特征值的项
# print(trees.splitDataSet(myDat,0,1))

# 选择最适合分类的一个特征
# print(trees.chooseBestFeatureToSplit(myDat))

# 树结构 字典
# print(trees.createTree(myDat,labels))

# 画出树结构
# treePlotter.createPlot()

# 树的节点数和深度
# print(treePlotter.getNumleafs(trees.createTree(myDat,labels)))
# print(treePlotter.getTreeDepth(trees.createTree(myDat,labels)))