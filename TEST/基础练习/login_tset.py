# -*-coding:utf-8 -*-
# Author:xmLi

import json
import sys

class Actual(object):
	'''登录主页'''

	def __init__(self):
		pass

	def out(self):
		'''账号，密码参数输出'''
		username = input('请输入账号：\n')
		password = input('请输入密码：\n')
		return username,password

	def registry(self):
		'''注册'''
		username,password = self.out()
		temp = username + "|" + password
		json.dump(temp, open('login.txt', 'w'))
		print('registry success!')

	def profile(self):
		'''个人主页'''
		lists = str(json.load(open('login.txt', 'r'))).split('|')
		print('欢迎{username}访问个人主页'.format(username=lists[0]))

	def login(self):
		'''登录'''
		usernama,password = self.out()
		lists = str(json.load(open('login.txt', 'r'))).split('|')
		if usernama == lists[0] and password == lists[1]:
			print('login success!')
			self.profile()
		else:
			print('账号或者密码错误')


	def main(self):
		while True:
			try:
				f=int(input('1、注册 2、登录 3、退出系统\n'))
				if f==1:
					self.registry()
				elif f==2:
					self.login()
				elif f==3:
					break
			except:
				continue

if __name__ == '__main__':
	obj = Actual()
	obj.main()





