from timeit import Timer

numList = []
for i in range(10000):
    numList.append(i)
def listnum(numList):
    theSum = 0
    for i in numList:
        theSum += i
    
    return theSum

def listnum2(numList,val):
    if len(numList) == 0:
        return val
    else:
        val += numList.pop()
        return listnum2(numList,val)

        


def listnum3(numList):
    if len(numList) == 1:
        return numList[0]

    else:
        return numList[0] + listnum3(numList[1:])


t1 = Timer("listnum([1,2,3,4,5])", "from __main__ import listnum")
t2 = Timer("listnum2([1,2,3,4,5],0)", "from __main__ import listnum2")
t3= Timer("listnum3([1,2,3,4,5])", "from __main__ import listnum3")
print("%f seconds \n"%t1.timeit(number=1000 ))
print("%f seconds \n"%t2.timeit(number=1000))
print("%f seconds \n"%t3.timeit(number=1000))

print(listnum([1,2,3,4,5]))
print(listnum2([1,2,3,4,5],0))
print(listnum3([1,2,3,4,5]))