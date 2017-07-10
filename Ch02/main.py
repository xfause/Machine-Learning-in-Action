import  kNN
import matplotlib
import  matplotlib.pyplot as plt
from numpy import *

# 获取运算所用的矩阵
# datingDataMat,datingLabels = kNN.file2maxtrix('datingTestSet2.txt')
# 因为作者的失误 datingTestSet.txt不能直接运行书中的代码
# 使用datingTestSet2.txt即可
# print(datingDataMat)
# print(datingLabels[0:20])

# 画散点图
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# add_subplot(x,y,z) x lines  y rows  z block
#ax.scatter(datingDataMat[:,1],datingDataMat[:,2],30.0*array(datingLabels),60.0*array(datingLabels))

# 根据不同的属性，从属性中取两个获得图，选择不同的属性分辨出数据属于的类别的性质更好。
# 15.0*datingLabels equals s=15.0
# s is a num of point size 
# ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
# plt.show()

#归一化
# normMat,ranges,minVal = kNN.autoNorm(datingDataMat)
# print(normMat)

# 测试约会数据
# kNN.datingClassTest()

# 测试手写数字
kNN.handWritingClassTest()