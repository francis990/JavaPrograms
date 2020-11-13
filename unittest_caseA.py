#coding=utf-8
import unittest


class unittest_caseA(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("all before A")


    def setUp(self):
        print("pre-condition of A")

    def testfirst01(self):
        self.assertEqual(1,1)
        print("A first case performed")
    def testfirst02(self):
        print("A second case performed")    
    def tearDown(self):
        print("after-condition of A")
    @classmethod
    def tearDownClass(self):
        print("all after A")
