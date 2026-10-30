import math

from geometric_lib.errors import NegativeValue
from geometric_lib.errors import negative_value_msg


def area(r: int) -> float:
    """
    Возвращает площадь круга в формате числа с плавающей точкой.

            Параметры:
                    r (int): радиус круга

            Возвращаемое значение:
                    area (float): площадь круга с радиусом r

            Пример вызова:
                    area(5) -> 78.53981633974483
    """
    if r < 0:
        raise NegativeValue(negative_value_msg)
    return math.pi * r * r


def perimeter(r: int) -> float:
    """
    Возвращает периметр круга в формате числа с плавающей точкой.

            Параметры:
                    r (int): радиус круга

            Возвращаемое значение:
                    perimeter (float): периметр круга с радиусом r

            Пример вызова:
                    perimeter(5) -> 31.41592653589793
    """
    if r < 0:
        raise NegativeValue(negative_value_msg)
    return 2 * math.pi * r
