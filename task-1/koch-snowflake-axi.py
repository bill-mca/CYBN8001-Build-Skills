import axi
from random import random

A4_PORT = (0, 0, 8.25, 11.75) # A4 Portrait bounds
A4_LAND = (0, 0, 11.75, 8.25) # A4 Landscape bounds
BOUNDS = A4_PORT 
# Set this variable to true when you wish to draw with the plotter.
draw = False

## Basic Letter A
def letter_a():
  t.left(120)
  t.forward(100)
  t.left(120)
  t.forward(100)
  t.left(180)
  t.forward(50)
  t.left(300)
  t.forward(50)
  
def axes():
  t.home()
  t.goto(200,0)
  t.home()
  t.goto(-200, 0)
  t.home()
  t.goto(0, 200)
  t.home()
  t.goto(0, -200)

#def target(distance, coordinate, heading):
    

def side(t, levels, length):
  md = length/3
  if levels == 0:
    t.forward(length)
  else:
    side(t, levels-1, length/3)
    t.left(60)
    side(t, levels-1, md)
    t.right(120)
    side(t, levels-1, md)
    t.left(60)
    side(t, levels-1, md)

#def side_coords(levels, length, coords, heading):
#  md = length/3
#  if levels == 0:
#    coords.append(target(length, coords[-1], heading))
#  else:
    

def koch(t, levels, length):    
	side(t, levels, length)
	t.right(120)
	side(t, levels, length)
	t.right(120)
	side(t, levels, length)
	t.right(120)
  
if __name__ == '__main__':
    t = axi.Turtle()
    #t.speed(10) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
    #t.right(30)
    side_length = 10000
    #koch(t, 0, side_length)
    koch(t, 1, side_length)
    koch(t, 2, side_length)
    koch(t, 3, side_length)
    koch(t, 4, side_length)
    koch(t, 5, side_length)
    #axes()
    #koch(t, 8, side_length)

    drawing = t.drawing.rotate_and_scale_to_fit(
        BOUNDS[2], BOUNDS[3], step=300, padding=0.5)
    # Render drawing
    im = drawing.render()
    # Create an image file of the drawing
    im.write_to_png('out.png')
    #im.svg_dump('out.svg')
    # Draw with the plotter if relevant
    if draw:
        axi.draw(drawing)
