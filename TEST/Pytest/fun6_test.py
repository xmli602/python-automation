# -*-coding:utf-8 -*-
# Author:xmLi

# fixture基础-初始化和清理详解及举例

import pytest

# 执行顺序
@pytest.fixture()
def init():
	print('\n初始化数据')
	yield
	print('清理数据')

def test_one():
	print('测试步骤')

def test_two(init):
	print('测试步骤2')


# pytest-selenium插件，用于在UI自动化
# @pytest.fixture()
# def init(selenium): # 此处selenium 为webdriverd实例化后的对象
# 	selenium.maximize_window()
# 	selenium.implicitly_wait(3)
# 	selenium.get('http://www.baidu.com/')
# 	yield
# 	selenium.quit()
#
# def test_baidu_title(init,selenium):
# 	assert selenium.title == '百度一下，你就知道'
#
# if __name__ == '__main__':
#     pytest.main(["-s","-v",'fun6_test.py'])
