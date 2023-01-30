# -*-coding:utf-8 -*-
# Author:xmLi


import yaml
from common.public import filePath

class OperationYaml:
	'''操作yaml文件'''
	def readYaml(self):
		with open(filePath(),'r',encoding='gbk') as f:
			return list(yaml.safe_load_all(f))

