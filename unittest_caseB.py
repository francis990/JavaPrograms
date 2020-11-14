#coding=utf-8
import unittest


class unittest_caseB(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("all before B")

    def setUp(self):
        print("pre-condition of B")

    def testfirstB01(self):
        print("B first case performed")
    def testfirstB02(self):
        print("B second case performed") 

    def tearDown(self):
        print("after-condition of B")    
    @classmethod
    def tearDownClass(self):
        print("all after B")    