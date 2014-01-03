#!/usr/bin/env python

import unittest
from src.sample import *

class TestSample(unittest.TestCase):

    def setUp(self):
        self.sample1 = Sample(9, 'sample1')

    def test_constructor(self):
        self.assertEquals('Sample', self.sample1.__class__.__name__)
        self.assertEquals(9, self.sample1.index)
        self.assertEquals('sample1', self.sample1.sample_name)



##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSample))
    return suite

if __name__ == '__main__':
    unittest.main()
