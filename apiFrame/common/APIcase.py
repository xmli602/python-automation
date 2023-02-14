# -*-coding:utf-8 -*-
# Author:xmLi
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
# # a = {"name":"#name#","gender":"#gender#","parentId":"0","status":1}
# parame = {"name":"#name#","parentId":"1439791207755497479","siteCode":"500100"}
# print(case.replace_data(str(parame)),type(eval(case.replace_data(str(parame)))))