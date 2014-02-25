#!/usr/bin/env python

import unittest
from mock import Mock
from src.vcf import *

class TestVCF(unittest.TestCase):

    def setUp(self):
        self.vcf = VCF()

    def test_constructor(self):
        self.assertEquals('VCF', self.vcf.__class__.__name__)

    def setup_vcf_lines(self):
        self.header = "##FILTER=<ID=HARD_TO_VALIDATE,Description=MQ0 >= 4 && ((MQ0 / (1.0 * DP)) > 0.1)>"
        self.sample_line = "#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	Sample_A	Sample_B	Sample_C	Sample_D	Sample_E"
        self.snp = "seq01	10	0	G	T	49.79	PASS	AC=5;AF=0.074;AN=68	GT:AD:DP:GQ:PL	0/0:1,0:1:3:0,3,25	0/0:2,0:2:6:0,6,45	0/0:6,0:6:18:0,18,138	0/0:6,0:6:18:0,18,138	0/0:6,0:6:18:0,18,138"

    def test_is_header(self):
        self.setup_vcf_lines()
        self.assertTrue(is_header(self.header))
        self.assertFalse(is_header(self.sample_line))
        self.assertFalse(is_header(self.snp))

    def test_is_sample_line(self):
        self.setup_vcf_lines()
        self.assertFalse(is_sample_line(self.header))
        self.assertTrue(is_sample_line(self.sample_line))
        self.assertFalse(is_sample_line(self.snp))

    def test_is_snp(self):
        self.setup_vcf_lines()
        self.assertFalse(is_snp(self.header))
        self.assertFalse(is_snp(self.sample_line))
        self.assertTrue(is_snp(self.snp))

    def test_get_samples(self):
        self.setup_vcf_lines()
        samples = get_samples(self.sample_line)
        self.assertTrue('Sample_E' in samples)
        self.assertEqual(11, samples['Sample_C'])

    def test_vcf_from_file(self):
        vcf = vcf_from_file('sample_files/5samples_5snps.vcf')
        self.assertTrue(vcf)
        self.assertEqual(5, len(vcf.snps))
        self.assertTrue('Sample_C' in vcf.samples)
        


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestVCF))
    return suite

if __name__ == '__main__':
    unittest.main()
