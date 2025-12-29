from points_on_a_plane_class import Point

class Triangle:
    slots = ("_vertices",)
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        verts = (vertex1, vertex2, vertex3)
        if not all(isinstance(v, Point) for v in verts):
            raise TypeError("All vertices must be Point instances")
        # store as an immutable tuple
        self._vertices: tuple[Point, Point, Point] = verts

    def vertices(self) -> tuple[Point, Point, Point]:
        return self._vertices

    def sides(self) -> tuple[float, float, float]:
        v = self._vertices
        pairs = zip(v, (v[1], v[2], v[0]))
        return tuple(a.distance_from_point(b) for a, b in pairs)

    def perimeter(self) -> float:
        return sum(self.sides())

    def __repr__(self) -> str:
        v = self._vertices
        return f"Triangle({v[0]}, {v[1]}, {v[2]})"
    
if __name__ == "__main__":
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print("Sides:", triangle.sides())
    print("Perimeter:", triangle.perimeter())