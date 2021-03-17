# # Draws an hexagram centred in the window that displays it,
# # with the colour of the tips alternating red and blue.
# #
# # Written by Eric Martin for COMP9021

# import turtle

# t = turtle.Turtle()
# t.pencolor('blue')
# t.forward(100)
# # t.penup()
# t.left(60)
# t.pencolor('red')
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.left(60)
# t.pencolor('blue')
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.left(60)
# t.pencolor('red')
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.left(60)
# t.pencolor('blue')
# t.pendown()
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.left(60)
# t.pencolor('red')
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.left(60)
# t.pencolor('blue')
# t.forward(100)
# turtle.done()

# Draws an hexagram centred in the window that displays it,
# with the colour of the tips alternating red and blue.
#
# Written by Eric Martin for COMP9021

from turtle import *


edge_length = 150
angle = 120

def draw_triangle(colour):
    color(colour)
    for _ in range(3):
        forward(edge_length // 3)
        penup()
        forward(edge_length // 3)
        pendown()
        forward(edge_length // 3)
        left(angle)

# Make sure that the hexagram is centred horizontally in the window that displays it.
penup()
forward(- edge_length // 2)
pendown()
draw_triangle('red')
penup()
forward(edge_length // 3)
left(angle)
forward(2 * edge_length // 3)
left(180)
pendown()
draw_triangle('blue')
