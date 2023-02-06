# -*-coding:utf-8 -*-
# Author:xmLi

# C端用户投递

import pytest
from utils.operationDB import connSQL,cursorCre
from utils.opreationExcelN import OperationExcelN,ExcelVarles
from utils.operationYaml import OperationYaml
from common.public import *
from base.method import Requests
import json

obj = Requests()
excel = OperationExcelN()
yaml = OperationYaml()
cursor = cursorCre()


def job_data():
	'''获取投递基础数据,岗位id,企业id,hrid'''
	sql_data = '''
	select id as job_id,enterprise_id,hr_id from enterprise_job where hr_id <>'1000000000' and status = 3 and source =0 order by rand() limit 1 
'''
	cursor.execute(sql_data)
	result = cursor.fetchall()
	data_job = result[0]
	return data_job





@pytest.mark.parametrize('datas',excel.runs())
def test_deliver(datas,get_BC_token,get_userid):
	'''简历投递流程测试'''

	# 对请求参数为空以及做反序列化处理
	params = datas[ExcelVarles.params]
	if len(str(params).strip()) == 0:
		pass
	elif len(str(params).strip()) >= 0:
		params = json.loads(params)

	# 对请求头为空以及做反序列化处理
	header = datas[ExcelVarles.headers]
	if len(str(header).strip()) == 0:
		pass
	elif len(str(header).strip()) >= 0:
		header = json.loads(header)

	if datas[ExcelVarles.caseName] == '检查是否已发起聊天':
		# print(params,type(params))
		# params['hrId'] = job_data()['hr_id']
		# params['jobId'] = job_data()['job_id']
		# params['userId'] = get_userid
		header = json.loads(str(datas[ExcelVarles.headers]).replace('{token}', get_BC_token))
		# print(header,type(header))
		# print(params,type(params))
		a = json.dumps(params)
		a = json.loads(a)
		print(a,type(a))
		# r = obj.post(url=datas[ExcelVarles.caseUrl],json = params,headers = header)
		# print(r.json())


if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_deliver.py"])

