from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side_length):
        self.__side_length = side_length

    @property
    def side_length(self):
        return self.__side_length

    def get_width(self):
        return self.__side_length

    def get_height(self):
        return self.__side_length

    def get_area(self):
        return self.__side_length * self.__side_length

    def get_perimeter(self):
        return self.__side_length * 4

    def __repr__(self):
        return f"({self.__side_length})"

    def __hash__(self):
        return self.side_length

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__side_length == other.__side_length


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3

    @property
    def x1(self):
        return self.__x1

    @property
    def y1(self):
        return self.__y1

    @property
    def x2(self):
        return self.__x2

    @property
    def y2(self):
        return self.__y2

    @property
    def x3(self):
        return self.__x3

    @property
    def y3(self):
        return self.__y3

    def get_width(self):
        return max(self.__x1, self.__x2, self.__x3) - min(self.__x1, self.__x2, self.__x3)

    def get_height(self):
        return max(self.__y1, self.__y2, self.__y3) - min(self.__y1, self.__y2, self.__y3)

    def get_area(self):
        return (1 / 2) * abs(self.__x1 * (self.__y2 - self.__y3)
                             + self.__x2 * (self.__y3 - self.__y1)
                             + self.__x3 * (self.__y1 - self.__y2))

    def get_perimeter(self):
        side_length1 = math.sqrt((self.__x2 - self.__x1) ** 2 + (self.__y2 - self.__y1) ** 2)
        side_length2 = math.sqrt((self.__x3 - self.__x2) ** 2 + (self.__y3 - self.__y2) ** 2)
        side_length3 = math.sqrt((self.__x3 - self.__x1) ** 2 + (self.__y3 - self.__y1) ** 2)
        return side_length1 + side_length2 + side_length3

    def __repr__(self):
        return f"({self.__x1}; {self.__y1}; {self.__x2}; {self.__y2}; {self.__x3}; {self.__y3})"

    def __hash__(self):
        return hash((self.__x1, self.__y1, self.__x2, self.__y2, self.__x3, self.__y3,))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return (self.__x1 == other.__x1 and self.__y1 == other.__y1
                and self.__x2 == other.__x2 and self.__y2 == other.__y2
                and self.__x3 == other.__x3 and self.__y3 == other.__y3)


class Rectangle(Shape):
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__length

    def get_area(self):
        return self.__width * self.__length

    def get_perimeter(self):
        return 2 * (self.__width + self.__length)

    def __repr__(self):
        return f"({self.__width}; {self.__length})"

    def __hash__(self):
        return hash((self.__width, self.__length))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__width == other.__width and self.__length == other.__length


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def get_width(self):
        return self.__radius * 2

    def get_height(self):
        return self.__radius * 2

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

    def __repr__(self):
        return f"({self.__radius})"

    def __hash__(self):
        return self.__radius

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__radius == other.__radius
