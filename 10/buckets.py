numbers = range(1, 14)

buckets = {0: list(),
            1: [],
            2: []}
for x in xrange(len(numbers)):
    dif = abs(numbers[x] - numbers[len(numbers) - x - 1])
    for b in xrange(3):
        if dif in buckets[b]:
            continue
        else:
            buckets[b].append(x)

print buckets
