#! /usr/bin/env python

import sys, time

# Let the user define the number
valid_input = False
try:
    numbers = int(sys.argv[1])
    valid_input = True
except IndexError:
    print "You must enter an int"
except ValueError:
    print "Only ints are accepted"
if not valid_input:
    sys.exit()

start_time = time.time()
# Generate an array of valid perfect squares
psquares = [x*x for x in xrange(2, int((numbers + numbers-1)**.5)+1)] 

# Create a map where every number in our range is a key and the
# value is an array of values that would make a perfect square
# without repeating the key in the value.
squares = {}
for x in xrange(1, numbers+1):
    temp = []
    for y in xrange(1, numbers+1):
        if x != y and x + y in psquares:
            temp.append(y)
    squares[x] = temp

# BFS the squares tree breaking when the len == the range of 
# numbers that we have.
valid = []
for start in xrange(1, numbers+1):
    queue = [[start]]

    while queue:
        current = queue.pop(0)
        parent = current[-1]
        nodes = squares[parent]

        end = False
        for node in nodes:
            if node not in current and current[-1] + node in psquares:
                queue.append(current + [node])
            else:
                continue
            if len(queue[-1]) == numbers:
                end = True
                break

        if end:
            ps = queue.pop()
            if ps not in valid and ps[::-1] not in valid: 
                valid.append(ps)

# Show valid solutions
print "Took %s seconds to find %d solutions:" % (str(time.time() - start_time), len(valid))
for result in valid:
    print result
