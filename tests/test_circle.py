from geometric_lib import circle
from geometric_lib.errors import NegativeValueError
from geometric_lib.errors import negative_value_error_msg

import math
import unittest


class CircleTestCase(unittest.TestCase):
    def test_area_normal_value(self):
        res = circle.area(5)
        self.assertEqual(res, math.pi * 25)

    def test_perimeter_normal_value(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 2 * math.pi * 5)

    def test_area_zero_radius(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_perimeter_zero_radius(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_area_big_radius(self):
        res = circle.area(2**500)
        self.assertEqual(res, 2**1000 * math.pi)

    def test_perimeter_big_radius(self):
        res = circle.perimeter(2**500)
        self.assertEqual(res, 2 * math.pi * 2**500)

    def test_area_negative_radius(self):
        with self.assertRaises(NegativeValueError) as context:
            circle.area(-100)
        self.assertEqual(str(context.exception), negative_value_error_msg)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(NegativeValueError) as context:
            circle.perimeter(-100)
        self.assertEqual(str(context.exception), negative_value_error_msg)
