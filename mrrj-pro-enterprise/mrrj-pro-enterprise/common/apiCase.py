#!/usr/bin/env python
#coding:utf-8

"""
@File    :   apiCase.py
@Time    :   2023/01/28
@Author  :   zhuoyan
@Contact :   18108347985@163.com
@Desc    :   请求体封装
"""

import re

class APICase:

    def replace_data(self, my_string):
        """替换 #value# 标记"""
        result = re.finditer('#(.+?)#', my_string)
        for el in result:
            target = el.group()  # #smsflag#
            print(target)
            prop = el.group(1)  #
            print(prop)
            value = getattr(self, prop)
            print(value)
            my_string = my_string.replace(target, value)
        return my_string


case = APICase()
# case.name = '李晓曼'
# case.gender = '女'
# case.parentId = "1"
# a = {"name":"#name#","gender":"#gender#","parentId":"0","status":1}
# print(case.replace_data(str(a)))
