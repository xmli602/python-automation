# -*-coding:utf-8 -*-
# Author:xmLi

import xlrd
import os
from xlutils.copy import copy

def base_dir(filename=None):
	return os.path.join(os.path.dirname(__file__),filename)

work = xlrd.open_workbook(base_dir('test.xls'))
sheet = work.sheet_by_index(0)
print(sheet.nrows)
print(sheet.cell_value(3,1))