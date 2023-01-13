# -*-coding:utf-8 -*-
# Author:xmLi

class Factory(object):
	def createObj(self,obj):
		if obj == 'apple':
			return Apple()
		elif obj == 'huawei':
			return HuaWei()

class Phone(object):
	pass

class Apple(Phone):
	def __str__(self):
		return 'apple'

	def show(self):
		print('苹果公司')

class HuaWei(Phone):
	def __str__(self):
		return 'huawei'

	def info(self):
		print('华为公司')

if __name__ == '__main__':
	factory = Factory()
	objApple = factory.createObj(obj='apple')
	objApple.show()


