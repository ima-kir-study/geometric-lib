from geometric_lib.errors import NegativeValue
from geometric_lib.errors import negative_value_msg


def area(a: int) -> int:
    '''
    Возвращает площадь квадрата в формате целого числа.

            Параметры:
                    a (int): сторона квадрата

            Возвращаемое значение:
                    area (int): площадь квадрата со стороной a

            Пример вызова:
                    area(5) -> 25
    '''
    if a < 0:
        raise NegativeValue(negative_value_msg)
    return a * a


def perimeter(a: int) -> int:
    '''
    Возвращает периметр квадрата в формате целого числа.

            Параметры:
                    a (int): сторона квадрата

            Возвращаемое значение:
                    perimeter (int): периметр квадрата со стороной a

            Пример вызова:
                    perimeter(5) -> 20
    '''
    if a < 0:
        raise NegativeValue(negative_value_msg)
    return 4 * a

