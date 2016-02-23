# -*- coding: utf-8 -*- 
'''
    testhelloworld.py

    Copyright (c) 2016 Shriram K
'''
import unittest
import helloworld

class TestStringMethods(unittest.TestCase):
	'''
	Test cases for hello world program
	'''
	def test_split(self):
		'''
		Tests hello world print statement function
		'''
		helloworld_obj = helloworld.HelloWorld()
		s = helloworld_obj.get_statement()
		self.assertEqual(s, 'hello world')
		self.assertEqual(s.split(), ['hello', 'world'])

if __name__ == '__main__':
    unittest.main()
