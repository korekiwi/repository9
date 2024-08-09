from abc import abstractmethod


class Figure:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return 'some figure'

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Figure):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)

    def __str__(self):
        return ('*' * self.width + '\n') * self.height

    def calculate_area(self):
        return self.width * self.height


class Circle(Figure):
    def __init__(self, radius: int):
        self.radius = radius

    def __str__(self):
        return f'ball with r = {self.radius}'

    def calculate_area(self):
        return self.radius ** 2 * 3.14


class Triangle(Figure):
    def __init__(self, side: int, height: int):
        self.side = side
        self.height = height

    def __str__(self):
        return f'triangle with side = {self.side} and height = {self.height}'

    def calculate_area(self):
        return 0.5 * self.side * self.height


class RightTriangle(Triangle):
    def __init__(self, a: int, b: int):
        super().__init__(a, b)

    def __str__(self):
        return f'triangle with a = {self.side} and b = {self.height}'


class Trapezoid(Figure):
    def __init__(self, a: int, b: int, h: int):
        self.a = a
        self.b = b
        self.h = h

    def __str__(self):
        return f'trapezoid with a = {self.a}, b = {self.b} and h = {self.height}'

    def calculate_area(self):
        return 0.5 * (self.a + self.b) * self.h


# rect = Rectangle(5, 2)
# print(rect)
#
# circle = Circle(5)
# print(circle.calculate_area())

# right_tr = RightTriangle(3, 4)
# print(right_tr)
#
# tr = Trapezoid(3, 5, 8)
# print(tr.calculate_area())


class Shape:
    def __int__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.draw = f'figure with coordinates of upper left angle: ' \
                    f'x: {self.x}, y: {self.y} \n'

    def show(self):
        print(self.draw)

    def save(self, file_name: str):
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(self.draw)

    @staticmethod
    def load(file_name: str):
        with open(file_name, 'r', encoding='utf-8') as f:
            return f.readlines()


class Square(Shape):
    def __init__(self, x: int, y: int, side: int):
        # super().__init__(x, y)
        self.x = x
        self.y = y
        self.side = side
        self.draw = f'Square with side = {self.side} and ' \
                    f'coordinates of upper left angle: x = {self.x}, y = {self.y} \n'


class Rectangle2(Shape):
    def __init__(self, x: int, y: int, width: int, height: int):
        # super().__init__(x, y)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.draw = f'Rectangle with width = {self.width} and height = {self.height} ' \
                    f'and coordinates of upper left angle: x = {self.x}, {self.y} \n'


class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int):
        # super().__init__(x, y)
        self.x = x
        self.y = y
        self.radius = radius
        self.draw = f'Circle with radius = {self.radius} and ' \
                    f'coordinates of centre: x = {self.x}, y = {self.y} \n'


class Ellipse(Shape):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.draw = f'Ellipse with coordinates of circumscribed rectangle: ' \
                    f'x = {self.x}, y = {self.y} and width and height of rectangle ' \
                    f'= {self.width}, {self.height} \n'


square = Square(1, 2, 5)
rect = Rectangle2(3, 4, 50, 60)
circle = Circle(7, 8, 50)
ellipse = Ellipse(5, 6, 10, 20)
figures = [square, rect, circle, ellipse]
fileName = 'figures.txt'

for i in figures:
    i.save(fileName)
    i.show()

new_figures = Shape.load(fileName)
print(new_figures)