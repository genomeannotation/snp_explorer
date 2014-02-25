#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.vcf import VCF, read_vcf 

class UIController:

    def __init__(self, vcf=None):
        self.vcf = vcf

    def read_vcf(self, filename):
        self.vcf = read_vcf(filename)


