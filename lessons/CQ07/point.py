"""Creating a point."""

from __future__ import annotations

__author__ = "730660492"


class Point:
    """Creating a point class."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Assinfing initial values for attributes."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method to mutate a point."""
        self.x = self.x * factor
        self.y = self.y * factor
    
    def scale(self, factor: int) -> Point:
        """Method to create a new point."""
        x = self.x * factor
        y = self.y * factor
        return Point(x, y)
    
    def __str__(self) -> str:
        """Print out points in a readable way."""
        my_point: str = f"x: {self.x}; y: {self.y}"
        return my_point
    
    def __mul__(self, factor: int | float) -> Point:
        """Overload the multiplication operator."""
        x = self.x * factor
        y = self.y * factor
        new_point = Point(x, y)
        return new_point
    
    def __add__(self, add: int | float) -> Point:
        """Overload the addition operator."""
        x = self.x + add
        y = self.y + add
        new_point1 = Point(x, y)
        return new_point1
