#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.call import *

def generate_snp(fulltext):
    all_fields = fulltext.split('\t')
    if len(all_fields) < 10:
        return None
    else:
        calls = []
        for raw_call in all_fields[9:]:
            calls.append(generate_call(raw_call))
        return SNP(all_fields[0], int(all_fields[1]), all_fields[3], all_fields[4], calls)

class SNP:

    def __init__(self, chrom, pos, ref, alt, calls):
        self.chrom = chrom
        self.position = pos
        self.reference = ref
        self.alternate = alt
        self.calls = calls

