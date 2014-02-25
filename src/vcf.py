#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys
from src.snp import SNP, generate_snp

def is_header(line):
    return line[0:2] == "##"

def is_sample_line(line):
    return line[0] == "#" and line[1] != "#"

def is_snp(line):
    splitline = line.split()
    return line[0] != "#" and len(splitline) > 9

def get_samples(line):
    samples = {}
    splitline = line.split()
    for i in xrange(9, len(splitline)):
        samples[splitline[i]] = i
    return samples

def read_vcf(iobuffer):
    headers = []
    snps = []
    samples = []

    for line in iobuffer:
        if is_header(line):
            headers.append(line)
        elif is_sample_line(line):
            samples = get_samples(line)
        elif is_snp(line):
            snps.append(generate_snp(line))
        else:
            sys.stderr.write("Error trying to read vcf file.")
            sys.stderr.write("The following line looks like neither header nor snp:\n" + line)

    return VCF(headers=headers, samples=samples, snps=snps)

class VCF:

    def __init__(self, headers=[], samples={}, snps=[]):
        self.headers = headers
        self.samples = samples
        self.snps = snps
    def __str__(self):
        result = "VCF with " + str(len(self.headers)) + " headers, "
        result += str(len(self.samples)) + " samples and "
        result += str(len(self.snps)) + " SNPs"
        return result
