class Things:
    pass
# To tell Python that a class is a child of another class, we add the name of the parent class in parentheses
class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    pass

class Mammals(Animals):
    pass

class Giraffes(Mammals):
    pass

reginald = Giraffes()
# Defining Functions of classes
# When we define a function that is associated with a class, we do so in the same way that we define any other function, except that we indent it beneath the class definition.
# def this_is_a_normal_function():
#   print('I am a normal function'):
# and this is a couple of fuctions that belongs to a class
# class ThisIsMySillyClass:
#    def this_is_a_normal_function():
#        print('I am a class function')
#    def this_is_also_a_class_function():
#        print('I am also a class function. See?')
class Animals(Animate):
    def breathe(self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass
class Mammals(Animals):
    def feed_young_with_milk(self):
        pass   
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        pass
# See how nothing will happen because we didnt define move, eat_leaves_from_trees yet
reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()
harold = Giraffes()
harold.move()
# Change out classes to make it a bit more obvious
class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')
reginald = Giraffes()
harold = Giraffes()
reginald.move()
harold.eat_leaves_from_trees()
# Objects and Classes in Pictures
import turtle
avery = turtle.Pen()
kate = turtle.Pen()
avery.forward(50)
avery.right(90)
avery.forward(20)
kate.left(90)
kate.forward(100)
jacob = turtle.Pen()
jacob.left(180)
jacob.forward(80)
# Need turtle.done() so it knows when to stop looking for commands this fixes it freezing. Will also stop VS code from insta-closing it
turtle.done()