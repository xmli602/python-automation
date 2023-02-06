# -*-coding:utf-8 -*-
# Author:xmLi


import yaml
from common.public import filePath
import json

class OperationYaml:
	'''操作yaml文件'''
	def readYaml(self):
		with open(filePath(),'r',encoding='gbk') as f:
			return list(yaml.safe_load_all(f))

	def dictYaml(self,fileDir='config',fileName='account.yaml'):
		'''读取yaml文件为字典类型'''
		with open(filePath(fileDir=fileDir,fileName=fileName),'r',encoding='gbk') as f:
			return yaml.load(f,Loader=yaml.FullLoader)

if __name__ == '__main__':
    obj = OperationYaml()
    items = obj.readYaml()
    print(items[0]['url'],type(items))
    # print(items['account_001']['telephone'])
    # print(type(items[1]['data']))
#     items = obj.dictYaml()
#


