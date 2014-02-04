#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

def create_samples_from_vcf_header(header):
    samples = []
    header_fields = header.split('\t')
    length = len(header_fields)
    if length < 10:
        return None
    else:
        for i in xrange(9, length):
            newsample = Sample(i, header_fields[i])
            samples.append(newsample)
        return samples


class Sample:

    def __init__(self, index, name):
        self.index = index
        self.sample_name = name


