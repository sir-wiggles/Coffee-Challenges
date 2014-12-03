import sys

n = int(sys.argv[1])

def without_zeros(n):
    while n>0:
        if n % 10 == 0:
            return False
        n /= 10
    return True


factors = sorted(filter(lambda x: without_zeros(x), set(
                reduce(list.__add__, ([i, n//i] for i in range(1, int(n**.5) + 1
                    ) if n % i == 0)))), reverse=True)

running = True
for x in factors:
    for y in factors:
        if x == y:
            continue
        else:
            if (x * y) == n:
                running = False
                break
    if not running:
        break

if x != y:
    print "Factors:", x, y
else:
    print "No Solution"
