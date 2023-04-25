a = [1,4,6]
b = [11,33,22]

c = list(b)
c.sort()
sorted = []

for i in c:
    for j in range(len(b)):
        if(b[j] == i):
            sorted.append(a[j])
print(sorted)
