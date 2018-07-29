a = ["banana", "apple", "microsoft"]
for element in a:
    print(element)
    print(element)
b = [20, 10, 5]
total = 0
for e in b:
    print(e)
    total = total + e
print(total)
c = list(range(1, 5))
print(c)
total2 = 0
for i in range(1, 5):
    total2 += i
print(total2)
print(list(range(1, 8)))
total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)
# All multiples of 3, 5 that are <100
total4 = 0
for i in (list(range(1, 100))):
    if i % 5 == 0:
        total4 += i
    elif i % 3 == 0:
        total4 += i
print(total4)
