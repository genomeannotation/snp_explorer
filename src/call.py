#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

def generate_call(fulltext):
    all_fields = fulltext.split(':')
    genotype = all_fields[0]
    if '/' not in genotype:
        return None
    else:
        return Call(fulltext, genotype)

class Call:

    def __init__(self, fulltext, genotype):
        self.fulltext = fulltext
        self.genotype = genotype

    def homozygous(self):
        alleles = self.genotype.split('/')
        if '.' in alleles:
            return False
        else:
            return alleles[0] == alleles[1]
        
    def heterozygous(self):
        alleles = self.genotype.split('/')
        return alleles[0] != alleles[1]

    def no_call(self):
        return '.' in self.genotype
