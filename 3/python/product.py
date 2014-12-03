numbers = '9876543210'

numbers = set()
for a in xrange(9, -1, -1):
    for b in xrange(8, -1, -1):
        for c in xrange(7, -1, -1):
            for d in xrange(6, -1, -1):
                for e in xrange(5, -1, -1):
                    for f in xrange(4, -1, -1):
                        for g in xrange(3, -1, -1):
                            for h in xrange(2, -1, -1):
                                for i in xrange(1, -1, -1):
                                    for j in xrange(1, -1, -1):
                                        number = []
#                                        if a == 9 and b == 6 and c == 4 and d == 2 and e == 0 and f == 0 and g == 0 and h ==0 and i == 0 and j == 0:
#                                            import pudb; pudb.set_trace()
                                        if a:
                                            number.append(a)
                                        if b and b not in number:
                                            number.append(b)
                                        if c and c not in number:
                                            number.append(c)
                                        if d and d not in number:
                                            number.append(d)
                                        if e and e not in number:
                                            number.append(e)
                                        if f and f not in number:
                                            number.append(f)
                                        if g and g not in number:
                                            number.append(g)
                                        if h and h not in number:
                                            number.append(h)
                                        if i and i not in number:
                                            number.append(i)
                                        if j and j not in number:
                                            number.append(j)
                                        if number:
                                            numbers.add(''.join(map(str, number)) )
                                        
numbers = map(int, list(set(numbers)))
test = numbers[:]
pre = numbers.pop()
max = [[0, [0, 0]]]
while numbers:
    print len(numbers)
    spre = set(str(pre))
    for x in numbers:
        if spre.intersection(set(str(x))):
            continue
        if x * pre > max[0][0]:
            max = [[x*pre,  [pre, x]]]
        elif x * pre == max[0][0]:
            max.append([x* pre, [pre, x]])
    pre = numbers.pop()

print max
