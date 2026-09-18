# Общее описание решения
Решение предоставляет инструменты для вычисления площадей и периметров
геометрических фигур. Реализована поддержка основных геометрических фигур:
прямоугольник, квадрат, треугольник и круг.

# Описание функций

Ниже приведено описание всех реализованных функций: их сигнатуры, а также
формулы, по которым производятся вычисления.

## Прямоугольник

### Формулы
- Площадь: $S = a \cdot b$
- Периметр: $P = (a + b) \cdot 2$

### Сигнатуры

```py
area(a: int, b: int) -> int
perimeter(a: int, b: int) -> int
```

## Квадрат

### Формулы
- Площадь: $S = a^2$
- Периметр: $P = 4 \cdot a$

### Сигнатуры

```py
area(a: int) -> int
perimeter(a: int) -> int
```

## Треугольник

### Формулы
- Площадь: $S = \frac{a \cdot h}{2}$
- Периметр: $P = a + b + c$

### Сигнатуры

```py
area(a: int, h: int) -> float
perimeter(a: int, b: int, c: int) -> int
```

## Круг

### Формулы
- Площадь: $S = \pi \cdot R^2$
- Периметр: $P = 2 \cdot \pi \cdot R$

### Сигнатуры

```py
area(r: int) -> float
perimeter(r: int) -> float
```

# История изменения проекта

```
63923b2 docs: add functions using examples
bf2ef3b docs(README): add functions description
70d7a6d docs(README): add general description of solution
7753bc9 docs(triangle): add docs for perimeter calc func
c7c5017 docs(triangle): add docs for area calc function
0401301 docs(square): add docs for perimeter calc function
c8285a2 docs(square): add docs for area calc function
efc4fcf docs(rectangle): add docs for perimeter calc func
a5f153e docs(rectangle): add docs for area calc function
2d00bc0 docs(circle): add docs for perimeter calc function
fd5944b docs(circle): add docs for area calc function
41edea9 fix(`rectangle.py`): correct fun to calc perimeter
2ce015b feat: add `triangle.py`
3edece4 feat: add `reactangle.py`
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
```

