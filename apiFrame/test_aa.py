# -*-coding:utf-8 -*-
# Author:xmLi

import pytest
from utils.opreationExcelN import OperationExcelN,ExcelVarles
from utils.operationYaml import OperationYaml
from common.public import *
from base.method import Requests
import json
import time
from datetime import datetime

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
	'''获取投递基础数据,岗位id,企业id,hrid,userid,简历id'''
	basics = {}
	sql_dels = [{'sql':"select id as jobId,enterprise_id as companyId,hr_id as hrId from enterprise_job where hr_id <>'1000000000' and status = 3 and source =0 order by rand() limit 1"},
	            {'sql':"select a.id as userId,b.id from rcw_user a LEFT JOIN resume b on a.id = b.user_id where a.telephone = {0}".format(yaml.readYaml()[0]['data']['account'])}]
	for sql in sql_dels:
		cursor.execute(sql['sql'])
		result = cursor.fetchall()
		basics.update(result[0])
	return basics

aa = job_data()

print(aa)

# params = { "sendId":"{user}","receiveId":"{hr_id}"}
#
# if 'sendId' or 'receiveId' in params.keys():
# 	params["sendId"] = job_data()["userId"]
# 	params["receiveId"] = job_data()["hrId"]

# sendTime = datetime.now().replace(microsecond=0)
# print(sendTime)




