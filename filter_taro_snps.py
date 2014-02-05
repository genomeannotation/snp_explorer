#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from src.snp import SNP, generate_snp
from src.call import Call
from src.group import Group
from src.sample import Sample, create_samples_from_vcf_header
import sys

def validate_command_line_argument(args):
    usage_message = "Usage: python filter_taro_snps.py <vcf_file>\n"
    if len(args) < 2:
        sys.stderr.write(usage_message)
        sys.exit()

vcf_file = sys.argv[1]
MIN_CALLS = 3

def is_comment(line):
    return line[0:2] == '##'

def is_header(line):
    return line[0:2] == '#C'

def resistant(sample):
    res_names = ['25_13', '25_96', '25_111', '25_129', '25_224', '25_281', '25_387', '25_507']
    for name in res_names:
        if name + ':' in sample.sample_name:
            return True
    return False

def nonresistant(sample):
    nonres_names = ['25_2', '25_40', '25_44', '25_56', '25_60', '25_64', '25_71', '25_72', '25_74', '25_114', '25_119', '25_120', '25_124', '25_125', '25_130', '25_131', '25_180', '25_186', '25_187', '25_204', '25_220', '25_234', '25_255', '25_274', '25_278', '25_283', '25_287', '25_288', '25_297', '25_302', '25_398', '25_418', '25_502', '25_509', '25_510']
    for name in nonres_names:
        if name + ':' in sample.sample_name:
            return True
    return False

def create_groups(samples):
    # for each sample, decide if it's univ.resist, univ. nonresist or other
    resist = []
    nonresist = []
    oth = []
    for sample in samples:
        if resistant(sample):
            resist.append(sample)
        elif nonresistant(sample):
            nonresist.append(sample)
        else:
            oth.append(sample)
    res = Group('Universally Resistant', resist)
    nonres = Group('Universally Nonresistant', nonresist)
    other = Group('Other', oth)
    return res, nonres, other

def snp_of_interest(snp, ingroup, outgroup, min_calls):
    #if snp.contains_heterozygous_call():
    #    return False
    if not snp.consistent_within_group(ingroup):
        return False
    elif not snp.consistent_within_group(outgroup):
        return False
    elif not snp.at_least_N_calls_in_group(min_calls, ingroup):
        return False
    elif not snp.at_least_N_calls_in_group(min_calls, outgroup):
        return False
    elif not snp.two_consistent_groups_differ(ingroup, outgroup):
        return False
    else:
        return True

def main():
    validate_command_line_argument(sys.argv)
    global MIN_CALLS
    with open(vcf_file, 'r') as vcf:
        for line in vcf:
            if is_comment(line):
                sys.stdout.write(line)
            elif is_header(line):
                sys.stdout.write(line)
                # create samples
                samples = create_samples_from_vcf_header(line)
                # create groups
                res, nonres, other = create_groups(samples)
            else:
                snp = generate_snp(line)
                print("we are at chrom " + snp.chrom + " pos " + str(snp.position))
                res_guys = snp.get_calls_from_group(res)
                res_calls = []
                for call in res_guys:
                    res_calls.append(call.genotype)
                nores_guys = snp.get_calls_from_group(nonres)
                nonres_calls = []
                for call in nores_guys:
                    nonres_calls.append(call.genotype)
                print("calls from resistant group are " + str(res_calls))
                print("calls from nonresistant group are " + str(nonres_calls))
                if snp and snp_of_interest(snp, res, nonres, MIN_CALLS):
                    sys.stdout.write(line)


####################################
if __name__ == '__main__':
    main()
