#!/usr/bin/env python

import unittest
from mock import Mock
from src.snp import *

class TestSNP(unittest.TestCase):

    def setUp(self):
        self.call1 = Mock()
        self.call2 = Mock()
        self.snp1 = SNP('seq1', 150, 'A', 'C', [self.call1, self.call2])

    def test_constructor(self):
        self.assertEquals('SNP', self.snp1.__class__.__name__)
        self.assertEquals('C', self.snp1.alternate)

    def test_generate_snp_good_data(self):
        # maybe should mock out generate_call function but too much trouble...
        snp = generate_snp("seq2\t125\t.\tG\tT\t30.7\tPASS\tblah_blah_info_field\tblah_blah_format_field\t0/0:1,0:1:3:0,3,26\t1/1:0,2:2:6:71,6,0\t./.")
        self.assertTrue(snp)
        self.assertEquals(3, len(snp.calls))
        self.assertEquals('G', snp.reference)
        self.assertEquals('T', snp.alternate)

    def test_generate_snp_bad_data(self):
        snp = generate_snp("seq2\t125\t.\tG\tT\t30.7\tPASS\tblah_blah_info_field")
        self.assertFalse(snp)


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSNP))
    return suite

if __name__ == '__main__':
    unittest.main()
