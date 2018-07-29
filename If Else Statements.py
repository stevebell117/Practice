# if else statements
# elif = else/if
a = 1
b = 2
if a < b:
    print("a is less than b")
    print("a is definitely less than b")
print("not sure if a is less than b")
c = 5
d = 4
if c < d:
    print("c is less than d")
else:
    print("c is not less than d")
    print("I don't think c is less than d")
print("outside the if block")
e = 20
f = 8
if e < f:
    print("e is less than f")
elif e == f:
    print("e is equal to f")
elif e > f + 10:
    print("e is greater than f by more than 10")
else:
    print("e is greater than f")
g = 8
h = 8
if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")
