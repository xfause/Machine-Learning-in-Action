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



