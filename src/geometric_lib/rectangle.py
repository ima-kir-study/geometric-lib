from geometric_lib.errors import NegativeValue
from geometric_lib.errors import negative_value_msg


def area(a: int, b: int) -> int:
    """
    Возвращает площадь прямоугольника в формате целого числа.

            Параметры:
                    a (int): первая сторона прямоугольника
                    b (int): вторая сторона прямоугольника

            Возвращаемое значение:
                    area (int): площадь прямоугольника со сторонами a и b

            Пример вызова:
                    area(5, 5) -> 25
    """
    if a < 0 or b < 0:
        raise NegativeValue(negative_value_msg)
    return a * b


def perimeter(a: int, b: int) -> int:
    """
    Возвращает периметр прямоугольника в формате целого числа.

            Параметры:
                    a (int): первая сторона прямоугольника
                    b (int): вторая сторона прямоугольника

            Возвращаемое значение:
                    perimeter (int): периметр прямоугольника со сторонами a и b

            Пример вызова:
                    perimeter(5, 5) -> 20
    """
    if a < 0 or b < 0:
        raise NegativeValue(negative_value_msg)
    return (a + b) * 2
