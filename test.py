class Point:
    def __init__(self,x):
        self.x = x
    @property
    def coord(self):
        return self.x

    @coord.setter
    def coord(self, x):
        self.x = x

pt = Point(1)

pt.coord = 2
print(pt.coord)

