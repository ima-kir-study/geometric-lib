import math


def area(r: int) -> float:
    '''
    Возвращает площадь круга в формате числа с плавающей точкой.

            Параметры:
                    r (int): радиус круга

            Возвращаемое значение:
                    area (float): площадь круга с радиусом r
    '''
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

