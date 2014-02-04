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

    def get_call_by_index(self, index):
        call_index = index - 9      # individual genotypes start at column 9
        if call_index < 0 or call_index >= len(self.calls):
            return None
        else:
            return self.calls[call_index]

    def get_calls_from_group(self, group):
        indices = group.get_indices()
        calls = []
        for index in indices:
            calls.append(self.get_call_by_index(index))
        return calls

    def at_least_N_calls_in_group(self, min_calls, group):
        all_calls = self.get_calls_from_group(group)
        calls = [c for c in all_calls if c.no_call() == False]
        return len(calls) >= min_calls

    def contains_heterozygous_call(self):
        for call in self.calls:
            if call.heterozygous():
                return True
        return False

    def consistent_within_group(self, group):
        calls = self.get_calls_from_group(group)
        if calls:
            first_genotype = calls.pop(0).genotype
            for call in calls:
                if call.genotype != first_genotype:
                    return False
            return True

