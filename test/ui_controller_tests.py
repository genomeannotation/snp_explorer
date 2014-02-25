#!/usr/bin/env python

import unittest
import io
from mock import Mock
from src.ui_controller import UIController

class TestUIController(unittest.TestCase):

    def setUp(self):
        pass
        self.controller = UIController()

    def test_constructor(self):
        self.assertEqual('UIController', self.controller.__class__.__name__)

    def test_read_vcf(self):
        self.assertFalse(self.controller.vcf)
        # TODO patch io and assert call instead of read real file
        self.controller.read_vcf("sample_files/5samples_5snps.vcf")
        self.assertTrue(self.controller.vcf)



##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestUIController))
    return suite

if __name__ == '__main__':
    unittest.main()
