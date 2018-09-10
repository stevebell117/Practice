# Parts of a function
# A function has three parts: Name, parameters, and a body.
# The name of this function is <testfunc>. It has a single parameter, <myname>, and its body is immediately following the line beginning with def (short for define)
def testfunc(myname):
    print('hello %s' % myname)
testfunc('Mary')
def testfunc(fname, lname):
    print('Hello %s %s' % (fname, lname))
testfunc('Mary', 'Smith')
firstname = 'Joe'
Lastname = 'Robertson'
testfunc(firstname, Lastname)
def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending
print(savings(10, 10, 5))
# Variables and scope
# A variable that’s inside the body of a function can’t be used again when the function has finished running because it exists only inside the function. In the world of programming, this is called scope.
another_variable = 100
def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable * another_variable
print(variable_test())
def spaceship_building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print('Week %s = %s cans' % (week, total_cans))
spaceship_building(2)
spaceship_building(13)
# Modules are used to group functions, variables, and other things together into larger, more powerful programs.
import time
print(time.asctime())
# sys.stdin.readline() is outdated I think
# import sys
# print(sys.stdin.readline())
# def silly_age_joke(age):
#     print('How old are you?')
#     age = int(sys.stdin.readline())
#     if age >= 10 and age <= 13:
#         print('What is 13 + 49 + 84 + 155 + 97? A headache!')
#     else:
#         print()
# Basic Moon Weight function
def moon_weight(weight, increase):
    for year in range(1, 16):
        weight = weight + increase
        moon_weight = weight * 0.165
        print('Year %s is %s' % (year, moon_weight))
moon_weight(40, 0.5)
# Moon weight function and years
def moon_weight(weight, increase, years):
    years = years + 1
    for year in range(1, years):
        weight = weight + increase
        moon_weight = weight * 0.165
        print('Year %s is %s' % (year, moon_weight))
moon_weight(35, 0.3, 5)