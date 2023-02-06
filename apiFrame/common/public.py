# -*-coding:utf-8 -*-
# Author:xmLi


import os

def filePath(fileDir='data',fileName='login.yaml'):
	'''
	:param fileDir: 目录
	:param fileName: 文件名称
	:return: 文件路径
	'''
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)

def writeFile(accountId):
	'''

	:param accountId: 账号id
	:return:
	'''
	with open('accountId','w') as f:
		f.write(str(accountId))

def readFile():
	'''
	读取账号id
	:return: 返回账号id
	'''

	with open('accountId','r') as f:
		return f.read()

