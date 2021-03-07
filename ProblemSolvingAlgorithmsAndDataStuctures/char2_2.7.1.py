import timeit
import random

for i in range(10000,1000001, 20000):
    t = timeit.Timer('index = random.randrange(%d); x[index]' % i, 'from __main__ import x, random')

    x = list(range(i))
    res = t.timeit()
    print("%d, %10.3f" % (i, res))


    