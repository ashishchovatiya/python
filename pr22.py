a = ((1, 2, 10, 9),('a','z','d','c'), (1, 4, 2, 3))
b = []
for i in range(len(a)):
    b.insert(i, list(a[i]))
    b[i].sort()
print(b)
b = tuple(b)
print(b)