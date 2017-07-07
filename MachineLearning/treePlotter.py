# -*- coding:utf-8 -*- 

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname="/usr/local/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/YaHei.ttf", size=10)

decisionNode = dict(boxstyle='sawtooth', fc='0.8')
leafNode = dict(boxstyle='round4', fc='0.8')
arrow_args = dict(arrowstyle='<-')

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
	createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords = 'axes fraction', xytext=centerPt, textcoords = 'axes fraction', va='center', ha='center', bbox=nodeType, arrowprops=arrow_args, fontproperties=font)

def createPlot():
	fig = plt.figure(1, facecolor='white')
	fig.clf()  # Clear the current figure.
	createPlot.ax1 = plt.subplot(111, frameon=False)
	plotNode('决策节点',  (0.5, 0.1), (0.1, 0.5), decisionNode)
	plotNode(u'叶节点',  (0.8, 0.1), (0.3, 0.8), leafNode)
	plt.title(u'标题', fontproperties=font)
	plt.show()

def getNumLeafs(myTree):
	numLeafs = 0
	firstStr = list(myTree.keys())[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			numLeafs += getNumLeafs(secondDict[key])
		else: numLeafs += 1
	return numLeafs
def getTreeDepth(myTree):
	maxDepth = 0
	firstStr = list(myTree.keys())[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			thisDepth = 1 + getTreeDepth(secondDict[key])
		else: thisDepth = 1
		if thisDepth > maxDepth: maxDepth = thisDepth
	return maxDepth

def retrieveTree(i):
	listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}, {'no surfacing': {0: 'no', 1: {'flippers': { 0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
	return listOfTrees[i]

def plotMidText(cntrPt, parentPt, txtString):
	xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
	yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
	createPlot.ax1.text(xMid, yMid, txtString)

def plotTree(myTree, parentPt, nodeTxt):
	numLeafs = getNumLeafs(myTree)
	depth = getTreeDepth(myTree)
	firstStr = list(myTree.keys())[0]
	cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/ 2.0 / plotTree.totalW, plotTree.yOff)