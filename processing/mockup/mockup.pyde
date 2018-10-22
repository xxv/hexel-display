import random

offset = PVector(50, 50)

class Cell(object):
    def __init__(self, x, y, cell_size):
        self._location = PVector(x, y)
        self._cell_size = cell_size
        self._color = (y * (100/41) + x * (100 / 14) / 2) % 256
        self._brightness = abs((y * (100/41) * 2 + x * (100 / 14)) % 256 - 128) * 2
        #self._brightness = random.random() * 255
        #self._color = random.random() * 255
        
    def display(self):
        pushMatrix()
        x = self._location.x * self._cell_size * 1.72
        y = self._location.y * self._cell_size * 1.5
        if self._location.y % 2 == 1:
            x += self._cell_size * 0.866
        
        translate(x, y)
        pushMatrix()

        rotate(PI/2)
        noStroke()
        fill(self._color, 255, abs(self._brightness - 128) * 2)
        self.polygon(0, 0, self._cell_size, 6)
        popMatrix()
        popMatrix()
        
    def update(self):
        self._brightness = (self._brightness + 0.5) % 256
        self._color = (self._color + 0.3) % 256
        
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
    size(660, 1230, P2D)
    colorMode(HSB)
    for y in range(0, 31):
        row = []
        grid.append(row)
        for x in range(0, 14 if y % 2 == 0 else 13):
            row.append(Cell(x, y, 25))
def draw():
    background(0)
    
    translate(offset.x, offset.y)
    
    for row in grid:
        for cell in row:
            cell.update()
            cell.display()
