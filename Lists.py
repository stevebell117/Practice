# append will add it to the end
#pop will take away the last thing in the list

a = [3, 10, -1]
print(a)
a.append(1)
print(a)
a.append("hello")
print(a)
a.append([1, 2])
print(a)
a.pop()
print(a)
a.pop()
print(a)
print(a[0])
print(a[3])
a[0] = 100
print(a)
b = ["banana", "apple", "microsoft"]
print(b)
temp = b[0]
b[0] = b[2]
print(b)
b[0], b[2] = b[2], b[0]
print(b)
