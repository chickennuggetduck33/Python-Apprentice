"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error
from tkinter import messagebox, simpledialog, Tk

# TODO)
#   1. Create a turtle.
dof = turtle.Turtle()
#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
def square():
    for i in range(4):
        dof.forward(13)
        dof.left(90)
def triangle():
    for i in range(3):
        dof.forward(13)
        dof.left(120)
def circle():
    dof.circle(8)
#   3. Ask the user for the for a shape to draw.
shape = simpledialog.askstring(None, prompt="shape")
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
if shape == "square":
    square()
elif shape == "triangle":
    triangle()
elif shape == "circle":
    circle()
turtle.done()
pass
