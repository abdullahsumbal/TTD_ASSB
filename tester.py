from unittest import TestCase

from PostalRateCalculator import RateCalculator
import sys


class TestSolver(TestCase):

    def no_args(self):
        s = RateCalculator(sys.argv)

        self.assertRaises(Exception, s.demo, 2, 1, 2)

    # def test_demo(self):
    #     self.fail()