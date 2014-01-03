#!/usr/bin/env python

import unittest
from src.call import *

class TestConsoleController(unittest.TestCase):

    def setUp(self):
        self.call1 = Call("0/0:1,0:1:3:0,3,26", "0/0")
        self.call2 = Call("1/1:0,2:2:3:45,3,0", "1/1")
        self.call3 = Call("0/1:1,2:3:25:57,0,25", "0/1")
        self.call4 = Call("./.", "./.")

    def test_constructor(self):
        self.assertEquals('Call', self.call1.__class__.__name__)
        self.assertEquals("0/0:1,0:1:3:0,3,26", self.call1.fulltext)
        self.assertEquals("1/1", self.call2.genotype)

    def test_homozygous(self):
        self.assertTrue(self.call1.homozygous())
        self.assertTrue(self.call2.homozygous())
        self.assertFalse(self.call3.homozygous())

    def test_homozygous_false_for_no_call(self):
        self.assertFalse(self.call4.homozygous())

    def test_heterozygous(self):
        self.assertFalse(self.call1.heterozygous())
        self.assertFalse(self.call2.heterozygous())
        self.assertTrue(self.call3.heterozygous())

    def test_no_call(self):
        self.assertFalse(self.call1.no_call())
        self.assertTrue(self.call4.no_call())

    def test_generate_call_good_data(self):
        call = generate_call("0/0:1,0:1:3:0,3,26")
        self.assertTrue(call)

    def test_generate_call_bad_data(self):
        call = generate_call("01,:835j/DF")
        self.assertFalse(call)






##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestConsoleController))
    return suite

if __name__ == '__main__':
    unittest.main()
