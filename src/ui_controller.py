#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.vcf import VCF, vcf_from_file

class UIController:

    def __init__(self, vcf=None):
        self.vcf = vcf

    def read_vcf(self, filename):
        self.vcf = vcf_from_file(filename)


