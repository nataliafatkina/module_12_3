from unittest import TestSuite, TestLoader, TextTestRunner
from  module_12_1 import RunnerTest
from module_12_2 import TournamentTest

test_suite = TestSuite()
test_suite.addTest(TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTest(TestLoader().loadTestsFromTestCase(TournamentTest))

runner = TextTestRunner(verbosity=2)
runner.run(test_suite)