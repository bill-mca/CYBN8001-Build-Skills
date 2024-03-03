import turtle
from random import random
t = turtle.Turtle()
t.speed(10) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

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

def koch(t, levels, length):    
	side(t, levels, length)
	t.right(120)
	side(t, levels, length)
	t.right(120)
	side(t, levels, length)
	t.right(120)
  

axes()
t.up()
t.goto(100, 0)
t.down()
letter_a()
t.pu()
t.goto(0, 0)
t.pd()
letter_a()
t.pu()
t.goto(0, -89)
t.pd()
letter_a()
t.pu()
t.goto(100, -89)
t.pd()
letter_a()

#axes()
t.right(30)
koch(t, 0, 200)
koch(t, 1, 200)
koch(t, 2, 200)
koch(t, 3, 200)
koch(t, 4, 200)