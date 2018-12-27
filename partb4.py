import unittest
import selenium1
import partb2
sample1_test = unittest.TestLoader().loadTestsFromModule(selenium1)
sample2_test = unittest.TestLoader().loadTestsFromModule(partb2)
cmd_test = unittest.TestSuite([sample1_test,sample2_test])

unittest.TextTestRunner(verbosity=2).run(cmd_test)