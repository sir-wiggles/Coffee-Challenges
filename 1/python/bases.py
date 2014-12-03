#! /usr/bin/env python

for x in xrange(10):
    for y in xrange(10):
        for z in xrange(10):
            if (x*100 + y*10 + z) == (z*81 + y*9 + x):
                print "X: %d, Y: %d, Z: %d" % (x, y, z)

