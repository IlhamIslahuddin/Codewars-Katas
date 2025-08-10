from preloaded import Point

def distance_between_points(a: Point, b: Point) -> float:
    return ((abs(a.x - b.x))**2 + (abs(a.y - b.y))**2 + (abs(a.z - b.z))**2)**0.5
