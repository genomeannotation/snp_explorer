#!/usr/bin/env python

import unittest
from src.call import Call

class TestConsoleController(unittest.TestCase):

    def setUp(self):
        self.call1 = Call("0/0:1,0:1:3:0,3,26", "0/0")
        self.call2 = Call("1/1:0,2:2:3:45,3,0", "1/1")
        self.call3 = Call("0/1:1,2:3:25:57,0,25", "0/1")

    def test_constructor(self):
        self.assertEquals('Call', self.call1.__class__.__name__)





##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestConsoleController))
    return suite

if __name__ == '__main__':
    unittest.main()
