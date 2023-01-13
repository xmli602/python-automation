# -*-coding:utf-8 -*-
# Author:xmLi

import json
import yaml
import csv
import xlrd

def readJson():
	'''读取json文件'''
	return json.load(open('test_data\login.json','r',encoding='utf-8')) # 读取json文件，数据类型为dic
	# return json.load(open('test_data\login.json','r',encoding='utf-8'))['item'] # 读取json文件下的列表，类型为list

# print(readJson(),type(readJson()))

def readYaml():
	'''读取yaml文件'''
	with open('test_data\login.yaml','r',encoding='utf-8') as f:
		return list(yaml.safe_load_all(f))


def readCsv():
	'''读取csv文件'''
	data = list()
	with open('test_data\login.csv','r',encoding='utf-8') as f:
		reader = csv.reader(f)
		next(reader)
		for item in reader:
			data.append(item)
	return data

def readExcel():
	'''读取excel文件'''
	data=list()
	book = xlrd.open_workbook('test_data\login.xlsx')
	sheet = book.sheet_by_index(0)
	for item in range(1,sheet.nrows):
		data.append(sheet.row_values(item))
	return data


# readExcel()
#
# for i in readExcel():
# 	data = i[1]
# 	print(data)
# 	print(type(data))


