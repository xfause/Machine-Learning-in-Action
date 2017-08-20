import trees
import treePlotter

fr = open('lenses.txt')
lensesLabels = ['age','prescript','astigmatic','tearRate']
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesTree = trees.createTree(lenses,lensesLabels)
treePlotter.createPlot(lensesTree)