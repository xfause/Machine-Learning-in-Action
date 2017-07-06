import  kNN
import matplotlib
import  matplotlib.pyplot as plt
from numpy import *

datingDataMat,datingLabels = kNN.file2maxtrix('datingTestSet2.txt')
# 因为作者的失误 datingTestSet.txt不能直接运行书中的代码
# 使用datingTestSet2.txt即可
print(datingDataMat)
print(datingLabels[0:20])
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# add_subplot(x,y,z) x lines  y rows  z block
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()