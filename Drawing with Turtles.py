# A module is a way of providing useful code to be used by another program among other things
import turtle
t = turtle.Pen()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
# t.reset clears the canvas and puts the turtle back at its starting position / t.clear just clears the screen and leaves the turle where it is
t.reset()
t.backward(100)
t.up()
t.right(90)
t.forward(20)
t.left(90)
t.down()
t.forward(100)
# Python for kids Pg 51 Puzzles 1 Rectangle
t.reset()
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
# Puzzle 2 Triangle
t.reset()
t.forward(30)
t.left(135)
t.forward(60)

# I dont yet know what this getscreen and mainloop are
turtle.getscreen()._root.mainloop()