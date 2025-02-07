class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        dibujo = ''
        if self.width <= 50 and self.height <= 50:
            for i in range(self.height):
                dibujo += '*' * self.width + '\n'
            return dibujo

        else:
            return 'Too big for picture.'

    def get_amount_inside(self, figure):
        if isinstance(self, Rectangle):
            return int(self.get_area() / figure.get_area())
        else:
            raise ValueError("The object has not similar naturalaze")

    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, s):
        self.width = s
        self.height = s

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):

        return f'Square(side={self.width})'

    def get_picture(self):
        dibujo = ''
        if self.width <= 50 and self.height <= 50:
            for i in range(self.height):
                dibujo += '*' * self.width + '\n'
            return dibujo

        else:
            return 'Too big for picture.'


r = Rectangle(4, 8)
print(r.get_area())
r2 = Rectangle(3, 6)
print(r2.get_area())
print(r.get_area() / r2.get_area())