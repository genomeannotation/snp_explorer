#!/usr/bin/env python

import unittest
from mock import Mock
from src.snp import *

class TestSNP(unittest.TestCase):

    def setUp(self):
        self.call1 = Mock()
        self.call2 = Mock()
        self.call3 = Mock()
        self.snp1 = SNP('seq1', 150, 'A', 'C', [self.call1, self.call2, self.call3])

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

    def test_get_call_by_index(self):
        self.assertEquals(self.call1, self.snp1.get_call_by_index(9))

    def test_get_call_by_index_out_of_range(self):
        no_call = self.snp1.get_call_by_index(20)
        self.assertFalse(no_call)

    def setup_group(self):
        self.group1 = Mock()
        self.group1.get_indices.return_value = [9, 11]
        self.group2 = Mock()
        self.group2.get_indices.return_value = [9, 10, 11]

    def test_get_calls_from_group(self):
        self.setup_group()
        calls = self.snp1.get_calls_from_group(self.group1)
        self.assertEquals(2, len(calls))

    def test_at_least_N_calls_in_group(self):
        self.setup_group()
        self.call1.no_call.return_value = False
        self.call2.no_call.return_value = True
        self.call3.no_call.return_value = False
        self.assertTrue(self.snp1.at_least_N_calls_in_group(2, self.group2))

    def test_at_least_N_calls_in_group_fails(self):
        self.setup_group()
        self.call1.no_call.return_value = True
        self.call2.no_call.return_value = True
        self.call3.no_call.return_value = False
        self.assertFalse(self.snp1.at_least_N_calls_in_group(2, self.group2))

    def test_contains_heterozygous_call(self):
        self.call1.heterozygous.return_value = False
        self.call2.heterozygous.return_value = True 
        self.call3.heterozygous.return_value = False
        self.assertTrue(self.snp1.contains_heterozygous_call())

    def test_contains_heterozygous_call_returns_false(self):
        self.call1.heterozygous.return_value = False
        self.call2.heterozygous.return_value = False
        self.call3.heterozygous.return_value = False
        self.assertFalse(self.snp1.contains_heterozygous_call())

        


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSNP))
    return suite

if __name__ == '__main__':
    unittest.main()
