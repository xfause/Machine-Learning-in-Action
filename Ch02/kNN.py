from numpy import *
import operator
from os import listdir

def createDataSet():
    group = array ( [ [1.0,1.1],[1.0,1.0],[0,0],[0,0.1] ] )
    lables = ['A','A','B','B']
    return group,lables

def classify(intX, dataSet, lables, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(intX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distance = sqDistance ** 0.5
    sortDistance = distance.argsort()

    classCount = {}
    for i in range(k):
        voteLable = lables[sortDistance[i]]
        classCount[voteLable] = classCount.get(voteLable,0)+1

    sortedClassCount = sorted(classCount.items(),
    key = operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def file2maxtrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classLabelVector

# 归一化 
# 避免由于不同类别的数据大小差距
# 导致某一类型的数值影响结果过大
# 转化为0-1 或 -1-1 之间
# newVal = (oldVal-min)/(max-min)
def autoNorm(dataSet):
    minVal = dataSet.min(0)
    maxVal = dataSet.max(0)
    ranges = maxVal - minVal
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVal,(m,1))
    # m lines 1 rows
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVal

# 内含的测试函数
# 自我引用 输出错误率
# file2Matrix & autoNorm read data and norm
# 确定用哪些数据做训练数据 哪些做测试数据
# classify分类
def datingClassTest():
    hoRatio = 0.1
    datingDataMat,datingLabels = file2maxtrix('datingTestSet2.txt')
    normMat,ranges,minVal = autoNorm(datingDataMat)
    m = normMat.shape[0]
    num4Test = int(hoRatio*m)
    errorCount = 0.0
    for i in range(num4Test):
        classifierResult = classify(normMat[i,:],normMat[num4Test:m,:],datingLabels[num4Test:m],3)
        print("the classifier came back with %d, real answer is %d" %(classifierResult,datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rating is %f" %(errorCount/float(num4Test)))


# img转化为向量 每个数字（0,1）代表一维
def img2Vector(filename):
    returnVec = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVec[0,i*32+j] = int(lineStr[j])
    return returnVec

#
def handWritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits') 
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
         fileNameStr = trainingFileList[i]
         fileStr = fileNameStr.split('.')[0] # take off .txt
         classNumStr = int(fileStr.split('_')[0])
         hwLabels.append(classNumStr)
         trainingMat[i,:] = img2Vector('trainingDigits/%s' % fileNameStr)

    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2Vector('testDigits/%s' % fileNameStr)
        classifierResult = classify(vectorUnderTest,trainingMat,hwLabels,3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): errorCount += 1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount/float(mTest)))