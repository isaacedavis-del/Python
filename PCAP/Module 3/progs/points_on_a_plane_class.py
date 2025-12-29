import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__coord = (self._to_float("x", x), self._to_float("y", y))

    def _to_float(self, name, value, finite=True):
        try:
            v = float(value)
        except (TypeError, ValueError) as e:
            raise TypeError(f"{name} must be a real number (convertible to float)") from e
        if finite and not math.isfinite(v):
            raise ValueError(f"{name} must be finite (got {v})")
        return v

    def x(self):
        return self.__coord[0]

    def y(self):
        return self.__coord[1]

    def distance_from_xy(self, x, y):
        x = self._to_float("x", x)
        y = self._to_float("y", y)
        return math.hypot(self.x() - x, self.y() - y)

    def distance_from_point(self, point):
        if not isinstance(point, Point):
            raise TypeError("point must be a Point")
        return math.hypot(self.x() - point.x(), self.y() - point.y())

if __name__ == "__main__":
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2))
    print(point2.distance_from_xy(2, 0))
