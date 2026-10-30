from geometric_lib import square
from geometric_lib.errors import NegativeValueError
from geometric_lib.errors import negative_value_error_msg

import unittest


class SquareTestCase(unittest.TestCase):
    def test_area_normal_value(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_perimeter_normal_value(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_area_zero_width(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_perimeter_zero_width(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_big_width(self):
        res = square.area(2**500)
        self.assertEqual(res, 2**1000)

    def test_perimeter_big_width(self):
        res = square.perimeter(2**500)
        self.assertEqual(res, 4 * 2**500)

    def test_area_negative_width(self):
        with self.assertRaises(NegativeValueError) as context:
            square.area(-100)
        self.assertEqual(str(context.exception), negative_value_error_msg)

    def test_perimeter_negative_width(self):
        with self.assertRaises(NegativeValueError) as context:
            square.perimeter(-100)
        self.assertEqual(str(context.exception), negative_value_error_msg)
