# -*-coding:utf-8 -*-
# Author:xmLi

# 参数化详解

'''针对列表中的对象循环，然后一一赋值，对象包括列表、元组、字典'''
import pytest

def add(a,b):
	return a+b

data = [
	pytest.param(1,1,2,id = 'one'),
	pytest.param(2,2,4,id = 'two'),
	pytest.param(3,3,6,id = 'three'),
	pytest.param(4,4,8,id = 'four')
]

# a,b,expect可以理解为被测函数的形式参数
@pytest.mark.parametrize('a,b,expect',data)
def test_add(a,b,expect):
	assert add(a,b) == expect