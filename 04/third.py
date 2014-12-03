
number_set = set(str(123456789))
n = 0
d = 0
while True:
    d += 3
    n += 1
    if not set(str(d)).intersection(set(str(n))):
        if  set(str(d)).union(set(str(n))) == number_set:
            break

print "%d/%d" % (n, d)
