# -*-coding:utf-8 -*-
# Author:xmLi

import pytest
import json
from utils.opreationExcelN import *
from common.public import *
from common.APIcase import *
from datetime import datetime
from base.method import Requests

obj = Requests()

@pytest.fixture()
def init(connSQL,cursorCre):
	connSQL
	yield
	# sql_claer = " DELETE from admin_dept where name = 'Auto一级0213' "
	print('数据清理')



@pytest.mark.parametrize('datas',execlN.runs())
def test_dept(init,datas,getToken,connSQL,cursorCre):
	'''

	:param datas: 所有可执行的测试用例
	:param getToken: 获取的运营端token
	:return:
	'''

	# 参数/请求头处理：为空，反序列化
	params = data_processing(datas[ExcelVarles.params])
	header = data_processing(datas[ExcelVarles.headers])
	# 获取token
	prevReault = getToken
	# 替换token
	header = execlN.prevHeaders(prevReault)
	# 状态码，期望结果断言
	r_code = int(datas[ExcelVarles.status_code])
	r_expect = str(datas[ExcelVarles.expect])
	def case_assert_result(rquest):
		'''
		封装断言，状态码和期望值
		:param rquest:
		:return:
		'''
		assert rquest.json()['code'] == r_code
		assert rquest.json()['message'] == r_expect
	case_pre = datas[ExcelVarles.casePre]
	casepre_list = str(case_pre).split('|')

	case.name_l1 = "Auto一级0213"
	case.name_l2 = "Auto二级0213"
	case.name_update = "Auto一级0213-编辑"
	case.name_update_repeat = "测试地方站（石柱站）"
	case.other_dept = '1472418994337308672'
	r = obj.post(url=datas[ExcelVarles.caseUrl], json=eval(case.replace_data(str(params))), headers=header)
	case_assert_result(r)
	if datas[ExcelVarles.caseName] == '新增一级部门':
		sql_getid = " SELECT id from admin_dept where name = 'Auto一级0213' "
		cursorCre.execute(sql_getid)
		first_order_id = cursorCre.fetchall()
		case.D_id_l1 = str(first_order_id[0]['id'])

		# if pre != '':
		# 	r_pre = obj.post(
		# 		url=execlN.case_prev(pre)[ExcelVarles.caseUrl],
		# 		# json=json.loads(execlN.case_prev(pre)[ExcelVarles.params]),
		# 		json=eval(case.replace_data(str(execlN.case_prev(pre)[ExcelVarles.params]))),
		# 		headers=header)
		# 	case_assert_result(r_pre)
		# 	sql_getid = " SELECT id from admin_dept where name = 'Auto一级0213' "
		# 	cursorCre.execute(sql_getid)
		# 	first_order_id = cursorCre.fetchall()
		# 	case.D_id = str(first_order_id[0]['id'])
		# 	r = obj.post(url=datas[ExcelVarles.caseUrl], json=eval(case.replace_data(str(params))), headers=header)
		# 	print(r.json())
		# 	case_assert_result(r)
		# else:
		# 	r = obj.post(url=datas[ExcelVarles.caseUrl], json=eval(case.replace_data(str(params))), headers=header)
		# 	case_assert_result(r)
		# 	sql_clear = "DELETE from admin_dept where name = 'Auto一级0213' "
		# 	cursorCre.execute(sql_clear)
		# 	connSQL.commit()
		# try:
		# 	if pre != '':
		# 		r_pre = obj.post(
		# 			url=execlN.case_prev(pre)[ExcelVarles.caseUrl],
		# 			json=json.loads(execlN.case_prev(pre)[ExcelVarles.params]),
		# 			headers=header)
		# 		print(r_pre.json())
		# 		sql_getid = " SELECT id from admin_dept where name = 'Auto一级0213' "
		# 		cursorCre.execute(sql_getid)
		# 		first_order_id = cursorCre.fetchall()
		# 		params = str(params).replace('{D_id}',str(first_order_id[0]['id']))
		# 		r = obj.post(url=datas[ExcelVarles.caseUrl], json=json.loads(params), headers=header)
		# 		print(r.json())
		# 	else:
		# 		# print('当前请求' + str(datas[ExcelVarles.caseUrl]) + '\n' + str(params))
		# 		r = obj.post(url=datas[ExcelVarles.caseUrl], json=params, headers=header)
		# 		print(r.json())
		# 		sql_clear = "DELETE from admin_dept where name = 'Auto一级0213' "
		# 		cursorCre.execute(sql_clear)
		# 		connSQL.commit()
		# except Exception as e:
		# 	print(str(datas[ExcelVarles.caseName]) + str(e))



if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_dept.py"])