#!/usr/bin/python3
"""Module that defines  a rectangle class """


class Rectangle:

    """Defines a rectangle object """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle object """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """string representation of the rectangle in # symbols """
        res = ""
        if self.area() == 0:
            return res
        for h in range(self.height):
            res += (self.width * str(self.print_symbol)) + "\n"
        return res[:-1]

    def __repr__(self):
        """str representation that can officially create the object """
        return "Rectangle({}, {})".format(str(self.width), str(self.height))

    def __del__(self):
        """Deletes the rectangle object """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter and setter to the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter and setter to the width attribute """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle """
        return self.height * self.width

    def perimeter(self):
        """Perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.height + 2 * self.width

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns biggest rectangle based on area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_2 if rect_2.area() > rect_1.area() else rect_1

    @classmethod
    def square(cls, size=0):
        """class method that returns new rect instance """
        return cls(size, size)
