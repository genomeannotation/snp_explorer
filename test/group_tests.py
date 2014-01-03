#!/usr/bin/env python

import unittest
from mock import Mock
from src.group import *

class TestGroup(unittest.TestCase):

    def setUp(self):
        self.sample1 = Mock()
        self.sample2 = Mock()
        self.sample3 = Mock()
        self.group1 = Group('group1', [self.sample1, self.sample2, self.sample3])

    def test_constructor(self):
        self.assertEquals('Group', self.group1.__class__.__name__)
        self.assertEquals(3, len(self.group1.samples))
        self.assertEquals('group1', self.group1.group_name)

    def test_get_names(self):
        self.sample1.sample_name = 'sample1'
        names = self.group1.get_names()
        self.assertEquals(3, len(names))
        self.assertTrue('sample1' in names)

    def test_get_indices(self):
        self.sample1.index = 9
        self.sample2.index = 10
        self.sample3.index = 11
        indices = self.group1.get_indices()
        self.assertEquals(3, len(indices))
        self.assertEquals([9, 10, 11], indices)


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGroup))
    return suite

if __name__ == '__main__':
    unittest.main()
