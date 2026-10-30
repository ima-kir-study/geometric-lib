from geometric_lib import rectangle
from geometric_lib.errors import NegativeValueError
from geometric_lib.errors import negative_value_error_msg

import unittest


class RectangleTestCase(unittest.TestCase):
    def test_area_normal_values(self):
        res = rectangle.area(5, 5)
        self.assertEqual(res, 25)

    def test_perimeter_normal_values(self):
        res = rectangle.perimeter(5, 5)
        self.assertEqual(res, 20)

    def test_area_zero_height(self):
        res = rectangle.area(0, 100)
        self.assertEqual(res, 0)

    def test_perimeter_zero_height(self):
        res = rectangle.perimeter(0, 100)
        self.assertEqual(res, 200)

    def test_area_zero_width(self):
        res = rectangle.area(100, 0)
        self.assertEqual(res, 0)

    def test_perimeter_zero_width(self):
        res = rectangle.perimeter(100, 0)
        self.assertEqual(res, 200)

    def test_area_big_height(self):
        res = rectangle.area(2**500, 100)
        self.assertEqual(res, 2**500 * 100)

    def test_perimeter_big_height(self):
        res = rectangle.perimeter(2**500, 100)
        self.assertEqual(res, 2 * (2**500 + 100))

    def test_area_big_width(self):
        res = rectangle.area(100, 2**500)
        self.assertEqual(res, 2**500 * 100)

    def test_perimeter_big_width(self):
        res = rectangle.perimeter(100, 2**500)
        self.assertEqual(res, 2 * (2**500 + 100))

    def test_area_negative_width(self):
        with self.assertRaises(NegativeValueError) as context:
            rectangle.area(-100, 100)
        self.assertEqual(str(context.exception), negative_value_error_msg)

    def test_area_negative_height(self):
        with self.assertRaises(NegativeValueError) as context:
            rectangle.area(100, -100)
        self.assertEqual(str(context.exception), negative_value_error_msg)

    def test_perimeter_negative_width(self):
        with self.assertRaises(NegativeValueError) as context:
            rectangle.perimeter(-100, 100)
        self.assertEqual(str(context.exception), negative_value_error_msg)

    def test_perimeter_negative_height(self):
        with self.assertRaises(NegativeValueError) as context:
            rectangle.perimeter(100, -100)
        self.assertEqual(str(context.exception), negative_value_error_msg)
