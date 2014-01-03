#!/usr/bin/env python

# import all the lovely files
import unittest
import test.call_tests
import test.snp_tests

# get suites from test modules
suite1 = test.call_tests.suite()
suite2 = test.snp_tests.suite()

# collect suites in a TestSuite object
suite = unittest.TestSuite()
suite.addTest(suite1)
suite.addTest(suite2)

# run suite
unittest.TextTestRunner(verbosity=2).run(suite)
