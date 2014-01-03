#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


class Group:

    def __init__(self, name, samples):
        self.group_name = name
        self.samples = samples


    def get_names(self):
        names = []
        for sample in self.samples:
            names.append(sample.sample_name)
        return names

    def get_indices(self):
        indices = []
        for sample in self.samples:
            indices.append(sample.index)
        return indices

