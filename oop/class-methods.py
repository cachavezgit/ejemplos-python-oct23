class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, coords): # cls is Point
        return cls(*coords) # <--- devuelve una instancia de la clase Point

    @classmethod
    def from_point(cls, point): # cls is Point
        return cls(point.x, point.y)
    
    @classmethod
    def from_coords(cls, x,y): # cls is Point
        return cls(x, y)
    
p = Point.from_tuple((3,7))
print(p.x, p.y) # 3 7

q = Point.from_point(p)
print(q.x, q.y) # 3 7

r = Point.from_coords(9,8)
print(r.x, r.y) # 3 7