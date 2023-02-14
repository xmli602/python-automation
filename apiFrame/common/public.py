# -*-coding:utf-8 -*-
# Author:xmLi


import os
import pymysql
import json

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


def cursorCre():
	'''数据库游标实例化'''
	db = pymysql.connect(host="192.168.18.168", port=3306, user="lixiaoman", password="lxm@123!", database="cq_rcw_new")
	cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
	return cursor

def  data_processing(data):
	'''
	处理测试用例中的数据：为空处理，序列化处理
	:param data: 需要处理的数据
	:return:
	'''
	global data_prod
	if len(str(data).strip()) == 0:
		pass
	elif len(str(data).strip()) >= 0:
		data_prod = json.loads(data)

	return data_prod



