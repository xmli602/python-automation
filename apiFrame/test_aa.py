# -*-coding:utf-8 -*-
# Author:xmLi

import pytest
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

# def test_001(get_BC_token,get_userid):
# 	print(get_userid)
#
# if __name__ == '__main__':
# 	pytest.main(["-s", "-v", "test_aa.py"])

def job_data():
	'''获取投递基础数据,岗位id,企业id,hrid'''
	sql_data = '''
	select id as job_id,enterprise_id,hr_id from enterprise_job where hr_id <>'1000000000' and status = 3 and source =0 order by rand() limit 1 
'''
	cursor.execute(sql_data)
	result = cursor.fetchall()
	data_job = result[0]
	return data_job

print(job_data())