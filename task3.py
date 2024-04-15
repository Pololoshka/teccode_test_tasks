"""
Создать класс Point, который представляет собой точку в двумерном пространстве.
Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки,
а также для получения и изменения координат.
"""

from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True, slots=True)
class Point:
    x: float | int
    y: float | int

    def calculate_distance(self, point: "Point") -> float:
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def __add__(self, point: "Point") -> Self:
        return self.__class__(x=self.x + point.x, y=self.y + point.y)

    def __sub__(self, point: "Point") -> Self:
        return self.__class__(x=self.x - point.x, y=self.y - point.y)


if __name__ == "__main__":
    point1 = Point(3, 5)
    point2 = Point(10, 7)
    point3 = Point(13, 12)
    point4 = Point(7, 2)

    assert round(point1.calculate_distance(point2), 3) == 7.28
    assert point1 + point2 == point3
    assert point2 - point1 == point4
