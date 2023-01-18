# -*-coding:utf-8 -*-
# Author:xmLi

import pytest
import requests
import read_data

# 实例，人才网运营端新增账号模块
data = read_data.readJson()

def connClose(connSQL):
	connSQL.close()

def wirteUserid(userID):
	with open('userId','w') as f:
		f.write(str(userID))

def getUserid():
	with open('userId','r') as f:
		return f.read()

@pytest.fixture()
def init(connSQL):
	connSQL
	yield
	connClose(connSQL)
	print('数据链接已关闭')

def test_addUser(getToken,init,connSQL,cursorCre):
	'''测试添加运营端用户'''
	r = requests.post(url=data["item"][1]["request"]["url"],
	                  json=data["item"][1]["request"]["body"],
	                  headers={'Authorization':'{0}'.format(getToken)})
	assert r.json()["code"] == 200
	assert r.json()["message"] == 'success'
	sql = "select * from admin_user where telephone = {0}".format(data["item"][1]["request"]["body"]["telephone"])
	cursorCre.execute(sql)
	result = cursorCre.fetchall()
	assert result[0]["telephone"] == data["item"][1]["request"]["body"]["telephone"]
	assert result[0]["dept_id"] == int(data["item"][1]["request"]["body"]["deptId"])
	assert result[0]["post"] == data["item"][1]["request"]["body"]["post"]
	assert result[0]["email"] == data["item"][1]["request"]["body"]["email"]

def test_getUser(getToken):
	'''测试新增的账户是否存在于用户列表'''
	r = requests.get(url='http://192.168.18.167:201/backend/system/user/pageUser?deptId=&name=&telephone={0}'.format(data["item"][1]["request"]["body"]["telephone"]),
	                 headers={'Authorization':'{0}'.format(getToken)})
	wirteUserid(r.json()["data"]["records"][0]["id"])
	assert r.json()["data"]["records"][0]["telephone"] == data["item"][1]["request"]["body"]["telephone"]

def test_delUser(getToken):
	'''测试运营端账号办理离职'''
	r = requests.get(url='http://192.168.18.167:201/backend/system/user/manageUser?id={0}&type=2'.format(getUserid()),
	                 headers={'Authorization':'{0}'.format(getToken)})
	assert r.status_code == 200

def test_userRecyclebin(getToken):
	'''测试已办理离职的账号是否在账号回收站'''
	r = requests.get(url='http://192.168.18.167:201/backend/system/user/pageResign?current=1&size=10&keyword={0}'.format(data["item"][1]["request"]["body"]["name"]),
	                 headers={'Authorization':'{0}'.format(getToken)})
	assert r.json()["data"]["records"][0]["name"] == data["item"][1]["request"]["body"]["name"]


if __name__ == '__main__':
    pytest.main(["-s","-v",'test_account.py'])
