#!/usr/bin/env python

import unittest
from mock import Mock
from src.ui_controller import UIController

class TestUIController(unittest.TestCase):

    def setUp(self):
        self.controller = UIController()

    def test_constructor(self):
        self.assertEquals('UIController', self.controller.__class__.__name__)

    def test_read_vcf(self):
        self.controller.vcf = Mock()
        self.controller.read_vcf('sample_files/5samples_5snps.vcf')



##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestUIController))
    return suite

if __name__ == '__main__':
    unittest.main()
