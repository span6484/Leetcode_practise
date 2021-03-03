from timeit import Timer

x = list(range(2000000))

popZero = Timer("x.pop(0)", "from __main__ import x")

popend = Timer("x.pop()", "from __main__ import x")
a = popZero.timeit(number = 1000)
b = popend.timeit(number = 1000)
print("Pop zero time is %f" %a)
print("Pop zero time is %f" %b)