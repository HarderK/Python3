import numpy as np

def loadDataSet():
	dataMat = []; labelMat = []
	fr = open('testSet.txt')
	for line in fr.readlines():
		lineArr = line.strip().split()
		dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
		labelMat.append([int(lineArr[2])])
	return dataMat, labelMat

def sigmoid(inX):
	return 1.0 / (1+np.exp(-inX))

# 梯度上升优化算法
def gradAscent(dataMatIn, classLabels):
	dataMatrix = np.mat(dataMatIn)
	labelMat = np.mat(classLabels)	
	m, n = np.shape(dataMatrix)
	alpha = 0.001	# 向目标移动的步长
	maxCycles = 500		# 迭代次数
	weights = np.ones((n, 1))
	for k in range(maxCycles):
		h = sigmoid(dataMatrix*weights)
		error = (labelMat - h)
		weights = weights + alpha * dataMatrix.transpose() * error
	return weights

def plotBestFit(wei):
	import matplotlib.pyplot as plt
	weights = wei
	dataMat, labelMat = loadDataSet()
	dataArr = np.array(dataMat)
	n = np.shape(dataArr)[0]
	xcord1 = []; ycord1 = []
	xcord2 = []; ycord2 = []
	for i in range(n):
		if int(labelMat[i][0]) == 1:
			xcord1.append(dataArr[i, 1]); ycord1.append(dataArr[i, 2])
		else:
			xcord2.append(dataArr[i, 1]); ycord2.append(dataArr[i, 2])
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
	ax.scatter(xcord2, ycord2, s=30, c='green')
	x = np.arange(-3.0, 3.0, 0.1)
	y = (-weights[0] - weights[1]*x) / weights[2]
	ax.plot(x, y)
	plt.xlabel('X1'); plt.ylabel('X2')
	plt.show()

# 随机梯度算法
def stocGradAscent0(dataMatrix, classLabels):
	m, n = np.shape(dataMatrix)
	alpha = 0.01
	weights = np.ones(n)
	for i in range(m):
		h = sigmoid(np.sum(dataMatrix[i] * weights))
		error = classLabels[i] - h
		weights = weights + alpha * error * dataMatrix[i]
	return weights

# 改进的随机梯度上升算法
def stocGradAscent1(dataMatrix, classLabels, numIter = 150):
	m, n = np.shape(dataMatrix)
	weights = np.ones(n)
	for j in range(numIter):
		dataIndex = list(range(m))
		for i in range(m):
			alpha = 4/(1.0+j+i) + 0.01 	# alpha在每次迭代的时候都进行调整，缓解高频波动,值越来越小，但不为0
			randIndex = int(np.random.uniform(0, len(dataIndex)))	# 随机抽取样本
			h = sigmoid(np.sum(dataMatrix[randIndex] * weights))
			# h = np.ones(n)
			error = classLabels[randIndex] - h
			weights = weights + alpha * error * dataMatrix[randIndex]
			del dataIndex[randIndex]
	return weights


def classifyVector(inX, weights):
	prob = sigmoid(np.sum(inX * weights))
	if prob > 0.5: 
		return 1.0
	else: 
		return 0.0

def colicTest():
	frTrain = open('horseColicTraining.txt')
	frTest = open('horseColicTest.txt')
	trainingSet = []; trainingLabels = []
	for line in frTrain.readlines():
		currLine = line.strip().split('\t')
		lineArr = []
		for i in range(21):
			lineArr.append(float(currLine[i]))
		trainingSet.append(lineArr)
		trainingLabels.append(float(currLine[21]))
	trainingWeights = stocGradAscent1(np.array(trainingSet), trainingLabels, 150)
	# print(trainingWeights)
	errorCount = 0; numTestVec = 0.0
	for line in frTest.readlines():
		numTestVec += 1.0
		currLine = line.strip().split('\t')
		lineArr = []
		for i in range(21):
			lineArr.append(float(currLine[i]))
		if int(classifyVector(np.array(lineArr), trainingWeights)) != int(currLine[21]):
			errorCount += 1
		errorRate = (float(errorCount) / numTestVec)
		print('the error rate of this test is : %f' % errorRate)
		return errorRate

def multiTest():
	numTests = 10; errorSum = 0.0
	for k in range(numTests):
		errorSum += colicTest()
	print('after %d iterations the average error rate is: %f' % (numTests, errorSum/float(numTests)))

colicTest()
