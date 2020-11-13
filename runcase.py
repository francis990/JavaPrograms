#coding=utf-8
#! /usr/bin/python
import unittest
import os
class runcase(unittest.TestCase):
    def test_case01(self):
        #case_path = os.path.join(os.getcwd(),'batch')  
        dir1="/home/francis/Desktop/fr2020/batch"
        suite = unittest.defaultTestLoader.discover(dir1,pattern='unittest_*.py')
        #suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        
        #print( case_path ) 
        unittest.TextTestRunner().run(suite)


if __name__=='__main__':
    unittest.main()
