#!/usr/bin/python3
"""module to define a rectangle
"""


class Rectangle:
    """defintion of an  rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """function initialisation
        Args:
            width: the first value
            height: the second value
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """function to get the width
        return: return the getting value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """function to set the width
        Args:
            value: the value to set
        raise:
            TypeError: if width is not an integer
            valueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """function to get the heigh
        return: return the getting value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """function to set the heigh
        Args:
            value: the value to set
        raise:
            TypeError: if height is not an integer
            valueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function to return the area of our rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """function to return the perimeter of our rectangle
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """function to print the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return None
        for i in range(self.__height):
            for j in range(self.__width):
                print(str(Rectangle.print_symbol), end="")
                if (i == (self.__height - 1) and j == (self.__width - 1)):
                    print("", end="")
                    break
                if (j == (self.__width - 1)):
                    print("")
        return ("")

    def __repr__(self):
        """function to behave as eval"""
        new = "Rectangle(" + str(self.__width)
        new += ", " + str(self.__height) + ")"
        return (new)

    def __del__(self):
        """function to print when an instance is delete
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
