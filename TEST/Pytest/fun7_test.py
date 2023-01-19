# -*-coding:utf-8 -*-
# Author:xmLi

# fixture pymql实例演示
import pymysql
import pytest

@pytest.fixture()
def connSQL():
	db = pymysql.connect(host="192.168.18.168",port=3306,user="lixiaoman",password="lxm@123!",database="cq_rcw_new")
	return db

def closeSql(connSQL):
	connSQL.close()

@pytest.fixture()
def cursorCre(connSQL):
	cursor = connSQL.cursor(cursor=pymysql.cursors.DictCursor)
	return cursor

@pytest.fixture()
def init(connSQL):
	connSQL
	yield
	closeSql(connSQL)

def test_getUser(init,connSQL,cursorCre):
	cursor = connSQL.cursor()
	sql = [{'sql':"select * from admin_user where telephone = {0}".format(18888888881)},{'sql':"select * from admin_user where telephone = {0}".format(15730332499)}]
	for i in sql:
		# print(i['sql'])
		cursorCre.execute(i['sql'])
		result = cursorCre.fetchall()
		print(result)


if __name__ == '__main__':
    pytest.main(["-s","-v",'fun7_test.py'])