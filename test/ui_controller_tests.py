#!/usr/bin/env python

import unittest
import io
from mock import Mock, patch
from src.ui_controller import UIController

class TestUIController(unittest.TestCase):

    def setUp(self):
        pass
        self.controller = UIController()

    def test_constructor(self):
        self.assertEqual('UIController', self.controller.__class__.__name__)

    # This test asserts that UIController.read_vcf opens the filename passed in
    # and calls read_vcf on the file returned.
    @patch('src.ui_controller.read_vcf')
    @patch('__builtin__.open')
    def test_read_vcf(self, mock_open, mock_read_vcf):
        mock_open.return_value = 'foo_file'
        self.assertFalse(self.controller.vcf)
        self.controller.read_vcf("imaginary_vcf")
        mock_open.assert_called_once_with("imaginary_vcf", 'r')
        mock_read_vcf.assert_called_with('foo_file')



##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestUIController))
    return suite

if __name__ == '__main__':
    unittest.main()
