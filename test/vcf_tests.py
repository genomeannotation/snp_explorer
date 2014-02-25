#!/usr/bin/env python

import unittest
import io
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

    def get_vcf_inputtext(self):
        inputtext = "##fileformat=VCFv4.1\n"
        inputtext += "##FILTER=<ID=HARD_TO_VALIDATE,Description=MQ0 >= 4 && ((MQ0 / (1.0 * DP)) > 0.1)>\n"
        inputtext += "#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	Sample_A	Sample_B	Sample_C	Sample_D	Sample_E\n"
        inputtext += "seq01	10	0	G	T	49.79	PASS	AC=5;AF=0.074;AN=68	GT:AD:DP:GQ:PL	0/0:1,0:1:3:0,3,25	0/0:2,0:2:6:0,6,45	0/0:6,0:6:18:0,18,138	0/0:6,0:6:18:0,18,138	0/0:6,0:6:18:0,18,138\n"
        inputtext += "seq01	25	0	T	A	481.57	PASS	AC=22;AF=0.344;AN=64	GT:AD:DP:GQ:PL	./.	0/1:3,1:4:11:11,0,54	1/1:0,5:5:15:113,15,0	1/1:0,5:5:15:113,15,0	1/1:0,5:5:15:113,15,0\n"
        inputtext += "seq02	20	0	G	A	32.95	PASS	AC=2;AF=0.032;AN=62	GT:AD:DP:GQ:PL	./.	0/0:5,0:5:15:0,15,114	0/0:5,0:5:15:0,15,113	./.	0/0:5,0:5:15:0,15,113\n"
        inputtext += "seq03	100	0	A	T	152.38	PASS	AC=14;AF=0.304;AN=46	GT:AD:DP:GQ:PL	./.	0/0:6,0:6:18:0,18,139	1/1:0,1:1:3:22,3,0	1/1:0,1:1:3:22,3,0	1/1:0,1:1:3:22,3,0\n"
        inputtext += "seq04	50	0	G	C	155.58	PASS	AC=4;AF=0.200;AN=20	GT:AD:DP:GQ:PL	./.	0/0:5,0:5:15:0,15,118	./.	./.	./."
        return inputtext

    def get_test_vcf(self):
        inputtext = self.get_vcf_inputtext()
        inputbuffer = io.BytesIO(inputtext)
        return read_vcf(inputbuffer)

    def test_read_vcf(self):
        vcf = self.get_test_vcf()
        self.assertTrue(vcf)
        self.assertEqual(5, len(vcf.snps))
        self.assertTrue('Sample_C' in vcf.samples)

    def test_constructor(self):
        vcf = VCF()
        self.assertEqual('VCF', vcf.__class__.__name__)

    def test_to_string(self):
        vcf = self.get_test_vcf()
        expected = "VCF with 2 headers, 5 samples and 5 SNPs"
        self.assertEqual(expected, str(vcf))


        


##########################
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestVCF))
    return suite

if __name__ == '__main__':
    unittest.main()
