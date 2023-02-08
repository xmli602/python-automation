# -*-coding:utf-8 -*-
# Author:xmLi

import pymysql
from utils.operationYaml import OperationYaml

yaml = OperationYaml()
# 投递基础数据准备hrid,jobid,userid,resumeid
db = pymysql.connect(host="192.168.18.168",port=3306,user="lixiaoman",password="lxm@123!",database="cq_rcw_new")
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
basics = {}
sql_dels = [{'sql': "select id as jobId,enterprise_id as companyId,hr_id as hrId from enterprise_job where hr_id <>'1000000000' and status = 3 and source =0 order by rand() limit 1"},
	        {'sql': "select a.id as userId,b.id from rcw_user a LEFT JOIN resume b on a.id = b.user_id where a.telephone = {0}".format(yaml.readYaml()[0]['data']['account'])}]
for sql in sql_dels:
	cursor.execute(sql['sql'])
	result = cursor.fetchall()
	basics.update(result[0])
