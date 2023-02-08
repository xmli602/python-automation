# -*-coding:utf-8 -*-
# Author:xmLi

# 封装excel操作工具
import xlrd
from common.public import filePath
from utils.operationYaml import OperationYaml

class ExcelVarles():
	'''定义excel的列'''
	caseId = 0
	description = 1
	url = 2
	method = 3
	data = 4
	expect = 5
	status_code = 6
	headers = 7

	def v_caseId(self):
		return self.caseId

	def v_description(self):
		return self.description

	def v_url(self):
		return self.url

	def v_method(self):
		return self.method

	def v_data(self):
		return self.data

	def v_except(self):
		return self.expect

	def v_status_code(self):
		return self.status_code

	def v_headers(self):
		return self.headers

class OperartionExcel(OperationYaml):
	'''操作excle文件'''
	def getSheet(self):
		account = xlrd.open_workbook(filePath(fileDir='data',fileName='deliver.xlsx'))
		return account.sheet_by_index(0)
	#
	# def getSheet(self,fileDir,fileName):
	# 	account = xlrd.open_workbook(filePath(fileDir=fileDir,fileName=fileName))
	# 	return account.sheet_by_index(0)


	@property
	def getRows(self):
		'''获取文件总行数'''
		return self.getSheet().nrows

	@property
	def getCols(self):
		'''获取文件总列数'''
		return self.getSheet().ncols

	def getValue(self,row,col):
		'''获取文件的值'''
		return self.getSheet().cell_value(row,col)

	def get_caseId(self,row):
		'''获取caseid'''
		return self.getValue(row=row,col=ExcelVarles().v_caseId())

	def get_description(self,row):
		'''获取case描述'''
		return self.getValue(row=row, col=ExcelVarles().v_description())

	def get_url(self,row):
		'''获取case请求地址'''
		url = self.getValue(row=row, col=ExcelVarles().v_url())
		return url

	def get_method(self,row):
		'''获取case请求方法'''
		return self.getValue(row=row, col=ExcelVarles().v_method())

	def get_data(self,row):
		'''获取case请求参数'''
		dataID = self.getValue(row=row, col=ExcelVarles().v_data())  # 获取excel中参数代号
		items = OperationYaml().dictYaml()
		return items[dataID]  # 返回对应代号的参数值
		# return self.getValue(row=row, col=ExcelVarles().v_data())

	def get_except(self,row):
		'''获取case期望结果'''
		return self.getValue(row=row, col=ExcelVarles().v_except())

	def get_status_code(self,row):
		'''获取case的响应码'''
		return self.getValue(row=row,col=ExcelVarles().v_status_code())

	def get_headers(self,row):
		'''获取case的响应码'''
		return self.getValue(row=row,col=ExcelVarles().v_headers())

if __name__ == '__main__':
    obj = OperartionExcel()
    print(obj.get_headers(1))

