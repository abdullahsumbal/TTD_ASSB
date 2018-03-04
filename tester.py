from unittest import TestCase

from PostalRateCalculator import RateCalculator
import sys


class TestSolver(TestCase):

    def test_no_args(self):
        R = RateCalculator([])
        self.assertEqual(R.cal(), "Usage: Python3 from_postal_code to_postal_code width height length weight post_type")

    def test_less_args(self):
        R = RateCalculator(["H2w1j5"])
        self.assertEqual(R.cal(), "Usage: Python3 from_postal_code to_postal_code width height length weight post_type")

    def test_more_args(self):
        R = RateCalculator([1,2,3,4,5,6,7,8])
        self.assertEqual(R.cal(), "Usage: Python3 from_postal_code to_postal_code width height length weight post_type")

    def test_correct_no_of_args(self):
        R = RateCalculator(['','','','','','',''])
        self.assertNotEqual(R.cal(), "Usage: Python3 from_postal_code to_postal_code width height length weight post_type")

    def test_len_from_postal_code(self):
        R = RateCalculator(["HeW1J534", 2, 3, 4, 5, 6, 7])
        self.assertEqual(R.cal(),"Invalid From: Postal Code")

    def test_wrong_from_postal_code_format(self):
        R = RateCalculator(["HeW1J5",2,3,4,5,6,7])
        self.assertEqual(R.cal(), "Invalid From: Postal Code")
        R = RateCalculator(["D2W155",2,3,4,5,6,7])
        self.assertEqual(R.cal(), "Invalid From: Postal Code")
        R = RateCalculator(["H2W145",2,3,4,5,6,7])
        self.assertEqual(R.cal(), "Invalid From: Postal Code")

    def test_len_to_postal_code(self):
        R = RateCalculator(["H2W1J5", "H2Wterer", 3, 4, 5, 6, 7])
        self.assertEqual(R.cal(),"Invalid To: Postal Code")

    def test_wrong_to_postal_code_format(self):
        R = RateCalculator(["H2W1J5","H23335",3,4,5,6,7])
        self.assertEqual(R.cal(), "Invalid To: Postal Code")
        R = RateCalculator(["H2W1J5","D2W155",3,4,5,6,7])
        self.assertEqual(R.cal(), "Invalid To: Postal Code")
        R = RateCalculator(["H2W1J5","H2W145",3,4,5,6,7])
        self.assertEqual(R.cal(), "Invalid To: Postal Code")

    def test_wrong_post_type(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "3", 4, 5, 6, "fjkldsf"])
        self.assertEqual(R.cal(),"Invalid Post Type: [Regular, Xpress, Prior]")
        R = RateCalculator(["H2W1J5", "H2W1J5", "3", "4", "5", "6", "Regular"])
        self.assertNotEqual(R.cal(), "Invalid Post Type: [Regular, Xpress, Prior]")

    def test_width_range(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "70", 4, 5, 6, "Regular"])
        self.assertEqual(R.cal(), "Invalid Width")
        R = RateCalculator(["H2W1J5", "H2W1J5", "-2", "4", 5, 6, "Prior"])
        self.assertEqual(R.cal(), "Invalid Width")
        R = RateCalculator(["H2W1J5", "H2W1J5", "50", 4, 5, 6, "Xpress"])
        self.assertEqual(R.cal(), "Invalid Width")

    def test_width_is_digit(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "fdf", "4", 5, 6, "Regular"])
        self.assertEqual(R.cal(), "Invalid Width")

    def test_heigth_is_digit(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", 'fdf', "5", "6", "Regular"])
        self.assertEqual(R.cal(), "Invalid Height")

    def test_height_range(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "0", "5", 6, "Regular"])
        self.assertEqual(R.cal(), "Invalid Height")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "51", 5, 6, "Prior"])
        self.assertEqual(R.cal(), "Invalid Height")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "-333", 5, 6, "Xpress"])
        self.assertEqual(R.cal(), "Invalid Height")

    def test_length_is_digit(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", '10', 'dfd', 6, "Regular"])
        self.assertEqual(R.cal(), "Invalid Length")

    def test_length_range(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "10", "-5", 6, "Regular"])
        self.assertEqual(R.cal(), "Invalid Length")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "11", "51", 6, "Prior"])
        self.assertEqual(R.cal(), "Invalid Length")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "33", "3335", 6, "Xpress"])
        self.assertEqual(R.cal(), "Invalid Length")

    def test_weight_is_digit(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", '10', '10',"0.565", "Regular"])
        self.assertEqual(R.cal(), "Invalid Weight")

    def test_weight_range(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "10", "5", "-6", "Regular"])
        self.assertEqual(R.cal(), "Invalid Weight")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "11", "50", "9996", "Prior"])
        self.assertEqual(R.cal(), "Invalid Weight")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "33", "35", "60", "Xpress"])
        self.assertEqual(R.cal(), "Invalid Weight")
