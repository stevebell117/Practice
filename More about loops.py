a = ["banana", "banana", "repiblic"]
for i in range(len(a)):
    for j in range(i + 1):
        # i = 0 -> j = 0
        # i = 1 -> j = 0, 1
        # i = 2 -> j = 0, 1, 2
        print(a[i])
# All multiples of 3, 5 that are <100
total = 0
for i in (list(range(1, 100))):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)
# Find the sum of the negative numbers
given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total2 = 0
j = len(given_list) - 1
while given_list[j] < 0:
    total2 += given_list[j]
    j -= 1
print(total2)
