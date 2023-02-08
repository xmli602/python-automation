# -*-coding:utf-8 -*-
# Author:xmLi

from base.method import Requests
from utils.opreationExcelN import ExcelVarles,OperationExcelN
from common.public import *
import pytest
import json
import ast
import allure



obj = Requests()
excel = OperationExcelN()

@pytest.mark.parametrize('datas',excel.runs())
def test_account(datas):
	# 对请求参数为空以及做反序列化处理
	params = datas[ExcelVarles.params]
	if len(str(params).strip()) == 0:
		pass
	elif len(str(params).strip()) >= 0:
		params = json.loads(params)
		# print(params)

	# 对请求头为空以及做反序列化处理
	header = datas[ExcelVarles.headers]
	if len(str(header).strip()) == 0:
		pass
	elif len(str(header).strip()) >= 0:
		header = json.loads(header)

	'''
	1、先获取到所有前置测试点的测试用例
	2、执行前置测试点
	3、前置测试点的结果信息
	4、将结果信息替换对应测试点的变量
	'''
	# 执行前置条件关联的测试点
	r = obj.post(
		url=excel.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.caseUrl],
		data=json.loads(excel.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.params])
	)
	prevResult = r.json()['data']['jwtToken']

	# 调用替换headers
	header = excel.prevHeaders(prevResult)

	status_code = int(datas[ExcelVarles.status_code])

	def case_assert_result(rquest):
		'''
		封装断言，状态码和期望值
		:param rquest: 请求
		:return:
		'''
		assert r.status_code == status_code
		assert datas[ExcelVarles.expect] in json.dumps(r.json(), ensure_ascii=False)

	def geturl():
		if datas[ExcelVarles.caseName] == '获取账号':
			return str(datas[ExcelVarles.caseUrl]).replace('{telephone}','18888888805')
		elif datas[ExcelVarles.caseName] == '账号离职':
			return str(datas[ExcelVarles.caseUrl]).replace('{ID}',readFile())


	if datas[ExcelVarles.caseMethod] == 'get':
		r = obj.get(url=geturl(), headers=header)
		case_assert_result(rquest=r)
		print(r.json())
		if datas[ExcelVarles.caseName] == '获取账号':
			writeFile(r.json()['data']['records'][0]['id'])
	elif datas[ExcelVarles.caseMethod] == 'post' and datas[ExcelVarles.paramsType] == 'data':
		r = obj.post(url=datas[ExcelVarles.caseUrl],data = params,headers = header)
		case_assert_result(rquest=r)
		print(r.json())
	elif datas[ExcelVarles.caseMethod] == 'post' and datas[ExcelVarles.paramsType] == 'json':
		if datas[ExcelVarles.caseName] == '编辑账号':
			params = str(params).replace('{accountId}',readFile())
			new_params = ast.literal_eval(params)  # 将参数从拼接后的str类型转为字典类型
			r = obj.post(url=datas[ExcelVarles.caseUrl],json = new_params,headers = header)
			case_assert_result(rquest=r)
			print(r.json())
		else:
			r = obj.post(url=datas[ExcelVarles.caseUrl],json = params,headers = header)
			case_assert_result(rquest=r)
			print(r.json())


if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_account_N.py","--alluredir","./report/result"])
	import subprocess
	subprocess.call('allure generate report/result/ -o report/html --clean',shell=True)
	subprocess.call('allure open -h 127.0.0.1 -p 8088 ./report/html',shell=True)
