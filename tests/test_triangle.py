from geometric_lib import triangle

import unittest


class TriangleTestCase(unittest.TestCase):
    def test_area_normal_values(self):
        res = triangle.area(5, 5)
        self.assertEqual(res, 5 * 5 / 2)

    def test_area_zero_heigth(self):
        res = triangle.area(100, 0)
        self.assertEqual(res, 0)

    def test_area_zero_base(self):
        res = triangle.area(0, 100)
        self.assertEqual(res, 0)

    def test_area_zero_heigth_and_base(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_area_big_height(self):
        res = triangle.area(2**500, 100)
        self.assertEqual(res, 2**500 * 100 / 2)

    def test_area_big_base(self):
        res = triangle.area(100, 2**500)
        self.assertEqual(res, 2**500 * 100 / 2)

    def test_area_big_height_and_base(self):
        res = triangle.area(2**500, 2**500)
        self.assertEqual(res, 2**500 * 2**500 / 2)

    def test_perimeter_normal_values(self):
        res = triangle.perimeter(5, 5, 5)
        self.assertEqual(res, 5 * 3)

    def test_perimeter_zero_first_side(self):
        res = triangle.perimeter(0, 5, 5)
        self.assertEqual(res, 10)

    def test_perimeter_zero_second_side(self):
        res = triangle.perimeter(5, 0, 5)
        self.assertEqual(res, 10)

    def test_perimeter_zero_third_side(self):
        res = triangle.perimeter(5, 5, 0)
        self.assertEqual(res, 10)

    def test_perimeter_zero_first_and_second_sides(self):
        res = triangle.perimeter(0, 0, 5)
        self.assertEqual(res, 5)

    def test_perimeter_zero_first_and_third_sides(self):
        res = triangle.perimeter(0, 5, 0)
        self.assertEqual(res, 5)

    def test_perimeter_zero_second_and_third_sides(self):
        res = triangle.perimeter(5, 0, 0)
        self.assertEqual(res, 5)

    def test_perimeter_zero_all_sides(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_big_first_side(self):
        res = triangle.perimeter(2**500, 5, 5)
        self.assertEqual(res, 2**500 + 10)

    def test_perimeter_big_second_side(self):
        res = triangle.perimeter(5, 2**500, 5)
        self.assertEqual(res, 2**500 + 10)

    def test_perimeter_big_third_side(self):
        res = triangle.perimeter(5, 5, 2**500)
        self.assertEqual(res, 2**500 + 10)

    def test_perimeter_big_first_and_second_sides(self):
        res = triangle.perimeter(2**500, 2**500, 5)
        self.assertEqual(res, 2**500 + 2**500 + 5)

    def test_perimeter_big_first_and_third_sides(self):
        res = triangle.perimeter(2**500, 5, 2**500)
        self.assertEqual(res, 2**500 + 2**500 + 5)

    def test_perimeter_big_second_and_third_sides(self):
        res = triangle.perimeter(5, 2**500, 2**500)
        self.assertEqual(res, 2**500 + 2**500 + 5)

    def test_perimeter_big_all_sides(self):
        res = triangle.perimeter(2**500, 2**500, 2**500)
        self.assertEqual(res, 2**500 + 2**500 + 2**500)
