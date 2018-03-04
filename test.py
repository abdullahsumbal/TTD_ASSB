from unittest import TestCase

from PRCalculator import RateCalculator


class TestSolver(TestCase):

    def test_no_args(self):
        R = RateCalculator([])
        self.assertEqual(R.cal(), "Usage: Python3 from_postal_code to_postal_code width length height weight post_type")

    def test_less_args(self):
        R = RateCalculator(["H2w1j5"])
        self.assertEqual(R.cal(), "Usage: Python3 from_postal_code to_postal_code width length height weight post_type")

    def test_more_args(self):
        R = RateCalculator(['1','2','3','4','5','6','7', '8'])
        self.assertEqual(R.cal(), "Usage: Python3 from_postal_code to_postal_code width length height weight post_type")

    def test_correct_no_of_args(self):
        R = RateCalculator(['','','','','','',''])
        self.assertNotEqual(R.cal(), "Usage: Python3 from_postal_code to_postal_code width length height weight post_type")

    def test_len_from_wrong(self):
        R = RateCalculator(["HeW1J534", '2','3','4','5','6','7'])
        self.assertEqual(R.cal(),"Invalid From: Postal Code")
        R = RateCalculator(["HeW4", '2','3','4','5','6','7'])
        self.assertEqual(R.cal(),"Invalid From: Postal Code")

    def test_len_from_correct(self):
        R = RateCalculator(["H2W1J5", '2','3','4','5','6','7'])
        self.assertNotEqual(R.cal(),"Invalid From: Postal Code")

    def test_from_postal_code_format_wrong(self):
        R = RateCalculator(["HeW1J5",'2','3','4','5','6','7'])
        self.assertEqual(R.cal(), "Invalid From: Postal Code")
        R = RateCalculator(["D2W155",'2','3','4','5','6','7'])
        self.assertEqual(R.cal(), "Invalid From: Postal Code")
        R = RateCalculator(["H2W145",'2','3','4','5','6','7'])
        self.assertEqual(R.cal(), "Invalid From: Postal Code")

    def test_from_postal_code_format_correct(self):
        R = RateCalculator(["H2W1J5",'2','3','4','5','6','7'])
        self.assertNotEqual(R.cal(), "Invalid From: Postal Code")

    def test_len_to_postal_code_wrong(self):
        R = RateCalculator(["H2W1J5", "H2Wterer", '3','4','5','6','7'])
        self.assertEqual(R.cal(),"Invalid To: Postal Code")
        R = RateCalculator(["H2W1J5", "H2Wt", '3','4','5','6','7'])
        self.assertEqual(R.cal(),"Invalid To: Postal Code")

    def test_len_to_postal_code_correct(self):
        R = RateCalculator(["H2W1J5", "H2W1G2", '3','4','5','6','7'])
        self.assertNotEqual(R.cal(),"Invalid To: Postal Code")

    def test_to_postal_code_format_wrong(self):
        R = RateCalculator(["H2W1G2",'H2W1fdsfG2','3','4','5','6','7'])
        self.assertEqual(R.cal(), "Invalid To: Postal Code")
        R = RateCalculator(["H2W1G2",'HEW1G2','3','4','5','6','7'])
        self.assertEqual(R.cal(), "Invalid To: Postal Code")
        R = RateCalculator(["H2W1G2",'H2W1G2FF','3','4','5','6','7'])
        self.assertEqual(R.cal(), "Invalid To: Postal Code")


    def test_wrong_post_type(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "3","4", '5', '6', "fjkldsf"])
        self.assertEqual(R.cal(),"Invalid Post Type: [Regular, Xpress, Prior]")

    def test_correct_post_type(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "3","4", '5', '6', "Xpress"])
        self.assertNotEqual(R.cal(),"Invalid Post Type: [Regular, Xpress, Prior]")
        R = RateCalculator(["H2W1J5", "H2W1J5", "3","4", '5', '6', "Prior"])
        self.assertNotEqual(R.cal(),"Invalid Post Type: [Regular, Xpress, Prior]")
        R = RateCalculator(["H2W1J5", "H2W1J5", "3","4", '5', '6', "Regular"])
        self.assertNotEqual(R.cal(),"Invalid Post Type: [Regular, Xpress, Prior]")

    def test_width_is_digit(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "0.4", "4", '5', '6', "Regular"])
        self.assertEqual(R.cal(), "Invalid Width")
        R = RateCalculator(["H2W1J5", "H2W1J5", "gfd34", "4",'5', '6', "Regular"])
        self.assertEqual(R.cal(), "Invalid Width")

    def test_width_range(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "70","4", '5', '6', "Regular"])
        self.assertEqual(R.cal(), "Invalid Width")
        R = RateCalculator(["H2W1J5", "H2W1J5", "-2", "4", '5', '6', "Prior"])
        self.assertEqual(R.cal(), "Invalid Width")
        R = RateCalculator(["H2W1J5", "H2W1J5", "51", "4", '5', '6',"Xpress"])
        self.assertEqual(R.cal(), "Invalid Width")

    def test_width_correct(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "10","4", '5', '6', "Regular"])
        self.assertNotEqual(R.cal(), "Invalid Width")
        R = RateCalculator(["H2W1J5", "H2W1J5", "50", "4", '5', '6', "Prior"])
        self.assertNotEqual(R.cal(), "Invalid Width")
        R = RateCalculator(["H2W1J5", "H2W1J5", "40", "4", '5', '6',"Xpress"])
        self.assertNotEqual(R.cal(), "Invalid Width")

    def test_length_is_digit(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", 'fre4545', '5', '6', "Regular"])
        self.assertEqual(R.cal(), "Invalid Length")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", '0.432434', '5', '6', "Regular"])
        self.assertEqual(R.cal(), "Invalid Length")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", '-0.432434', '5', '6', "Regular"])
        self.assertEqual(R.cal(), "Invalid Length")


    def test_length_range(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "10","1000", '5', '6', "Regular"])
        self.assertEqual(R.cal(), "Invalid Length")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "0", '5', '6', "Prior"])
        self.assertEqual(R.cal(), "Invalid Length")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "-4", '5', '6',"Xpress"])
        self.assertEqual(R.cal(), "Invalid Length")

    def test_length_correct(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "10","30", '5', '6', "Regular"])
        self.assertNotEqual(R.cal(), "Invalid Length")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "50", '5', '6', "Prior"])
        self.assertNotEqual(R.cal(), "Invalid Length")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "4", '5', '6',"Xpress"])
        self.assertNotEqual(R.cal(), "Invalid Length")

    def test_heigth_is_digit(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", '10', "fdsfsd", "6", "Regular"])
        self.assertEqual(R.cal(), "Invalid Height")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", '10', "0.5", "6", "Regular"])
        self.assertEqual(R.cal(), "Invalid Height")

    def test_height_range(self):
        R = RateCalculator(["H2W1J5", "H2W1J5", "10","10", '-5', '-6', "Regular"])
        self.assertEqual(R.cal(), "Invalid Height")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "10", '51', '51', "Prior"])
        self.assertEqual(R.cal(), "Invalid Height")
        R = RateCalculator(["H2W1J5", "H2W1J5", "10", "10", '1', '1',"Xpress"])
        self.assertEqual(R.cal(), "Invalid Height")