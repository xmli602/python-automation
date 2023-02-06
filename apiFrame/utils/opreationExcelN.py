# -*-coding:utf-8 -*-
# Author:xmLi

# 测试用例参数化的方式操作excel
import xlrd
from common.public import filePath
import json

class ExcelVarles:
	caseID = '测试用例ID'
	caseModel = '模块'
	caseName = '接口名称'
	caseUrl = '请求地址'
	casePre = '前置条件'
	caseMethod = '请求方法'
	paramsType = '请求参数类型'
	params = '请求参数'
	expect = '期望结果'
	isRun = '是否执行'
	headers = '请求头'
	status_code = '状态码'
	post_params = '后置参数'


class OperationExcelN():
	'''操作excel'''
	def getsheet(self):
		'''读取excel文件sheet'''
		case = xlrd.open_workbook(filePath(fileDir='data',fileName='delivertest.xlsx'))
		return case.sheet_by_index(0)

	@property
	def getRows(self):
		'''获取文件总行数'''
		return self.getsheet().nrows

	@property
	def getCols(self):
		'''获取文件中列数'''
		return self.getsheet().ncols

	@property
	def getExcelDates(self):
		'''获取excel所有用例数据，以字典类型写入到列表中'''
		accountcase = []
		title = self.getsheet().row_values(0)
		for row in range(1,self.getsheet().nrows):
			row_values = self.getsheet().row_values(row)
			accountcase.append(dict(zip(title,row_values)))  # 两个数据值以键值对形式组装，并转为字典类型
		return accountcase

	def cases_list(self):
		'''获取所有测试用例'''
		cases_list=[]
		for item in self.getExcelDates:
			cases_list.append(item)
		return cases_list

	def runs(self):
		'''获取可执行的测试用例'''
		run_list = []
		for item in self.getExcelDates:
			isRun = item[ExcelVarles.isRun]
			if isRun == 'y':
				run_list.append(item)
			else:
				pass
		return run_list

	def params(self):
		'''对请求参数为空进行处理'''
		params_list = []
		for item in self.runs():
			params = item[ExcelVarles.params]
			if len(str(params).strip()) == 0:pass
			elif len(str(params).strip()) >= 0:
				params_list.append(json.loads(params))
		return params_list

	def case_prev(self,casePrev):
		'''
		根据前置条件寻找关联case
		:param casePrev: 前置测试条件
		:return:
		'''
		for item in self.runs():
			# print(item.values())
			# print(item[ExcelVarles.casePre])
			if casePrev in item.values():
				return item
		return None

	def prevHeaders(self,prevResult):
		'''
		替换case的请求头变量的值
		:param prevResult:
		:return:
		'''
		'''
		1、获取headers
		'''
		for item in self.runs():
			headers = item[ExcelVarles.headers]
			if '{token}' in headers:
				headers = str(headers).replace('{token}',prevResult)
				return json.loads(headers)



if __name__ == '__main__':
    obj = OperationExcelN()
    for i in obj.cases_list():
	    print(i)

    # print(obj.prevHeaders('ces'))
    # print(obj.case_prev('login'))