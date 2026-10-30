# Общее описание решения

Решение предоставляет инструменты для вычисления площадей и периметров
геометрических фигур. Реализована поддержка основных геометрических фигур:
прямоугольник, квадрат, треугольник и круг.

# Описание функций

Ниже приведено описание всех реализованных функций: их сигнатуры, а также
формулы, по которым производятся вычисления.

## Прямоугольник

### Площадь

Возвращает площадь прямоугольника в формате целого числа.

#### Формула

```math
S = a \cdot b
```

#### Сигнатура

```py
area(a: int, b: int) -> int
```

#### Параметры

- `a (int)`: первая сторона прямоугольника
- `b (int)`: вторая сторона прямоугольника

#### Возвращаемое значение

- `area (int)`: площадь прямоугольника со сторонами `a` и `b`

#### Пример вызова

```py
area(5, 5) -> 25
```

### Периметр

Возвращает периметр прямоугольника в формате целого числа.

#### Формула

```math
P = (a + b) \cdot 2
```

#### Сигнатура

```py
perimeter(a: int, b: int) -> int
```

#### Параметры

- `a (int)`: первая сторона прямоугольника
- `b (int)`: вторая сторона прямоугольника

#### Возвращаемое значение

- `perimeter (int)`: периметр прямоугольника со сторонами `a` и `b`

#### Пример вызова

```py
perimeter(5, 5) -> 20
```

## Квадрат

### Площадь

Возвращает площадь квадрата в формате целого числа.

#### Формула

```math
S = a^2
```

#### Сигнатура

```py
area(a: int) -> int
```

#### Параметры

- `a (int)`: сторона квадрата

#### Возвращаемое значение

- `area (int)`: площадь квадрата со стороной `a`

#### Пример вызова

```py
area(5) -> 25
```

### Периметр

Возвращает периметр квадрата в формате целого числа.

#### Формула

```math
P = 4 \cdot a
```

#### Сигнатура

```py
perimeter(a: int) -> int
```
#### Параметры

- `a (int)`: сторона квадрата

#### Возвращаемое значение

- `perimeter (int)`: периметр квадрата со стороной `a`

#### Пример вызова

```py
perimeter(5) -> 20
```

## Треугольник

### Площадь

Возвращает площадь треугольника в формате числа с плавающей точкой.

#### Формула

```math
S = \frac{a \cdot h}{2}
```

#### Сигнатура

```py
area(a: int, h: int) -> float
```

#### Параметры

- `a (int)`: основание треугольника
- `h (int)`: высота треугольника

#### Возвращаемое значение

`area (float)`: площадь треугольника с основанием `a` и высотой `h`

#### Пример вызова

```py
area(5, 5) -> 12.5
```

### Периметр

Возвращает периметр треугольника в формате целого числа.

#### Формула
```math
P = a + b + c
```
#### Сигнатура

```py
perimeter(a: int, b: int, c: int) -> int
```
#### Параметры

- `a (int)`: первая сторона треугольника
- `b (int)`: вторая сторона треугольника
- `c (int)`: третья сторона треугольника

#### Возвращаемое значение

- `perimeter (int)`: периметр треугольника со сторонами `a`, `b` и `c`

#### Пример вызова

```py
perimeter(5, 5, 5) -> 15
```

## Круг

### Площадь

Возвращает площадь круга в формате числа с плавающей точкой.

#### Формула

```math
S = \pi \cdot R^2
```
#### Сигнатура

```py
area(r: int) -> float
```
#### Параметры

- `r (int)`: радиус круга

#### Возвращаемое значение

- `area (float)`: площадь круга с радиусом `r`

#### Пример вызова

```py
area(5) -> 78.53981633974483
```

### Периметр
Возвращает периметр круга в формате числа с плавающей точкой.

#### Формула

```math
P = 2 \cdot \pi \cdot R
```

#### Сигнатура
```py
perimeter(r: int) -> float
```

#### Параметры

- `r (int)`: радиус круга

#### Возвращаемое значение

- `perimeter (float)`: периметр круга с радиусом `r`

#### Пример вызова

```py
perimeter(5) -> 31.41592653589793
```

# Зависимости

- `uv`
- `python==3.12`

# Тесты

```
uv run coverage run -m unittest discover
uv run coverage report
```

# История изменения проекта

```
c3069d3 style: format the code with ruff
1712ff5 test: add tests to check negative values
fb90273 feat: raise exception if value is negative
ce8f394 docs(README): info about tests and requirements
eb1ef2d chore: add .coverage to .gitignore
3b436dd chore: install `coverage`
c5af1a4 chore: switch to UV
0e8d0ab test: add python package with tests
18dba90 chore: add .gitignore
9be1713 refactor: make a separate python package for app
8c21eb2 docs(README): add params, return values, examples
bf54784 docs(README): add project modification history
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

