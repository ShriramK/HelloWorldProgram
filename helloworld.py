# -*- coding: utf-8 -*- 
'''
    helloworld.py

    Copyright (c) 2016 Shriram K
'''

class HelloWorld:
	'''
	Hello World program that prints a statement
	'''
	_statement = 'hello world'
	def get_statement(self):
		return self._statement
	def print_statement(self):
		print self._statement

if __name__ == "__main__":
	hello_world_obj = HelloWorld()
	hello_world_obj.print_statement()
