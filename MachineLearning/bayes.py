# -*- coding:utf-8 -*- 

import numpy as np
# import re

# 词表到向量的转换函数
def loadDataSet():
	postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
	classVec = [0, 1, 0, 1, 0, 1]   # 1代表侮辱性言论    2代表正常言论
	return postingList, classVec

def createVocabList(dataSet):
	vocabSet = set([])
	for document in dataSet:
		vocabSet = vocabSet | set(document)    # 两个集合的并集
	return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
	returnVec = [0] * len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else: print('the word: %s is not in my Vocabulary!' % word)
	return returnVec

# 朴素贝叶斯词袋模型
def bagOfWords2VecMN(vocabList, inputSet):
	returnVec = [0] * len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] += 1
	return returnVec

# 分类器训练函数
def trainNB0(trainMatrix, trainCategory):
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])
	pAbusive = sum(trainCategory) / float(numTrainDocs)
	p0Num = np.ones(numWords); p1Num = np.ones(numWords)
	p0Denom = 2.0; p1Denom = 2.0
	for i in range(numTrainDocs):
		if trainCategory[i] == 1:
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])	# 分类为1的词的总数
		else: 
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
	p1Vect = np.log(p1Num / p1Denom)
	p0Vect = np.log(p0Num / p0Denom)
	return p0Vect, p1Vect, pAbusive


# 分类器
# vec2Classify  需要分类的向量文档
# p0Vect  词在类0中概率列表
# p1Vect  此在类1中的概率列表
# pClass1  训练文档中类1出现的概率
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
	# print('here', type(p1Vec))
	p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)
	p0 = sum(vec2Classify * p0Vec) + np.log(1.0 - pClass1)
	if p1 > p0:
		return 1
	else:
		return 0

def testingNB():
	listOPosts, listClasses = loadDataSet()
	myVocabList = createVocabList(listOPosts)
	trainMat = []
	for postinDoc in listOPosts:
		trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
	p0V, p1V, pAb = trainNB0(np.array(trainMat), np.array(listClasses))
	testEntry = ['love', 'my', 'dalmation']
	thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
	print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
	testEntry = ['stupid', 'garbage']
	thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
	print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))

# 将长文本解析为字符串列表
def textParse(bigString):
	import re
	listOfTokens = re.split(r'\W+', bigString)
	return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def spamTest():
	docList = []; classList = []; fullText = []
	for i in range(1, 26):
		wordList = textParse(open('email/spam/%d.txt' % i, encoding='windows-1252').read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(1)
		wordList = textParse(open('email/ham/%d.txt' % i, encoding='windows-1252').read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(0)
	# print(docList)
	vocabList = createVocabList(docList)
	trainingSet = list(range(50)); testSet = []
	for i in range(10):
		randIndex = int(np.random.uniform(0, len(trainingSet)))
		testSet.append(trainingSet[randIndex])
		del(trainingSet[randIndex])
	trainMat = []; trainClasses = []
	for docIndex in trainingSet:
		trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
		trainClasses.append(classList[docIndex])
	p0V, p1V, pSpam = trainNB0(np.array(trainMat), np.array(trainClasses))
	errorCount = 0
	for docIndex in testSet:
		wordVector = setOfWords2Vec(vocabList, docList[docIndex])
		if classifyNB(np.array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
			errorCount += 1
			print('classification error ', docList[docIndex])
	print('the error rate is: ', float(errorCount) / len(testSet))


# RSS源分类器
def calcMostRreq(vocabList, fullText):
	import operator
	freqDict = {}
	for token in vocabList:
		freqDict[token] = fullText.count(token)
	sortedFreq = sorted(freqDict.items(), key = operator.itemgetter(1), reverse=True)
	return sortedFreq[:30]

def localWords(feed1, feed0):
	import feedparser
	docList = []; classList = []; fullText = []
	minLen = min(len(feed1['entries']), len(feed0['entries']))
	for i in range(minLen):
		wordList = textParse(feed1['entries'][i]['summary'])
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(1)
		wordList = textParse(feed0['entries'][i]['summary'])
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(0)
	vocabList = createVocabList(docList)	
	top30Words = calcMostRreq(vocabList, fullText)
	for pairW in top30Words:
		if pairW[0] in vocabList: vocabList.remove(pairW[0]) # 去掉出现次数最高的词
	trainingSet = list(range(2*minLen)); testSet = []
	for i in range(20):
		randIndex = int(np.random.uniform(0, len(trainingSet)))
		testSet.append(trainingSet[randIndex])
		del(trainingSet[randIndex])
	trainMat = []; trainClasses = []
	for docIndex in trainingSet:
		trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
		trainClasses.append(classList[docIndex])
	p0V, p1V, pSpam = trainNB0(np.array(trainMat), np.array(trainClasses))
	errorCount = 0
	for docIndex in testSet:
		wordVector = setOfWords2Vec(vocabList, docList[docIndex])
		if classifyNB(np.array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
			errorCount += 1
			print('classification error ', docList[docIndex])
	print('the error rate is: ', float(errorCount) / len(testSet))

def getTopWords(ny, sf):
	import operator
	vocabList, p0V, p1V = localWords(ny, sf)
	topNY = []; topSF = []
	for i in range(len(p0V)):
		if p0V[i] > -0.6 : topSF.append((vocabList[i], p0V[i]))
		if p1V[i] > -0.6 : topNY.append((vocabList[i], p1V[i]))
	sortedSF = sorted(topSF, key = lambda: pair: pair[i], reverse = True)
	print('SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**')
	for item in sortedSF
		print(item[0])

# testingNB()
spamTest()
