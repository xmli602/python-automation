# -*-coding:utf-8 -*-
# Author:xmLi
import pytest
from base.method import Requests
from utils.operationYaml import OperationYaml
import json

obj = Requests()
objyaml = OperationYaml()

# 参数化，实现一个测试用例测试多个点
@pytest.mark.parametrize('datas',objyaml.readYaml())
def test_login(datas):
	'''测试登录成功'''
	r = obj.post(url=datas['url'],json=json.loads(datas['data']))
	# assert r.json()['message'] == datas['except']
	assert datas['except'] in json.dumps(r.json(),ensure_ascii=False)


if __name__ == '__main__':
    pytest.main(["-v","test_login.py"])