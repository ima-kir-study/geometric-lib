from geometric_lib.errors import NegativeValueError
from geometric_lib.errors import negative_value_error_msg


def area(a: int, h: int) -> float:
    """
    Возвращает площадь треугольника в формате числа с плавающей точкой.

            Параметры:
                    a (int): основание треугольника
                    h (int): высота треугольника

            Возвращаемое значение:
                    area (float): площадь треугольника с основанием a и высотой
                    h

            Пример вызова:
                    area(5, 5) -> 12.5
    """
    if a < 0 or h < 0:
        raise NegativeValueError(negative_value_error_msg)
    return a * h / 2


def perimeter(a: int, b: int, c: int) -> int:
    """
    Возвращает периметр треугольника в формате целого числа.

            Параметры:
                    a (int): первая сторона треугольника
                    b (int): вторая сторона треугольника
                    c (int): третья сторона треугольника

            Возвращаемое значение:
                    perimeter (int): периметр треугольника со сторонами a, b и c

            Пример вызова:
                    perimeter(5, 5, 5) -> 15
    """
    if a < 0 or b < 0 or c < 0:
        raise NegativeValueError(negative_value_error_msg)
    return a + b + c
