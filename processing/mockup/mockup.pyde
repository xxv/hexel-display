import random

offset = PVector(100, 100)

class Cell(object):
    def __init__(self, x, y, cell_size):
        self._location = PVector(x, y)
        self._cell_size = cell_size
        self._color = random.random() * 100
        
    def display(self):
        pushMatrix()
        x = self._location.x * self._cell_size * 1.72
        y = self._location.y * self._cell_size * 1.5
        if self._location.y % 2 == 0:
            x += self._cell_size * 0.866
        
        translate(x, y)
        pushMatrix()

        rotate(PI/2)
        noStroke()
        fill(0, 0, self._color)
        self.polygon(0, 0, self._cell_size, 6)
        popMatrix()
        popMatrix()
        
    def update(self):
        self._color = (self._color + 1) % 100
        
    def polygon(self, x, y, radius, npoints):
        angle = TWO_PI / npoints
        beginShape()
        
        for a in range(0, npoints):
            sx = x + cos(a * angle) * radius
            sy = y + sin(a * angle) * radius
            vertex(sx, sy)
        
        endShape(CLOSE)
        
    grid = []

def setup():
    size(1000, 1500, P2D)
    colorMode(HSB, 100)
    for y in range(0, 20):
        row = []
        grid.append(row)
        for x in range(0, 14):
            row.append(Cell(x, y, 30))
def draw():
    background(0)
    
    translate(offset.x, offset.y)
    
    for row in grid:
        for cell in row:
            cell.update()
            cell.display()
