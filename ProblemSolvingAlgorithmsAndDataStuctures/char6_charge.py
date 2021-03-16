#coding:utf-8
import time

#极其低效
def recMc(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1

    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMc(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
            
    return minCoins



#改进后

def recMc2(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1

    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMc2(coinValueList, change - i,knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

# print(time.clock())
# print(recMc([1,5,10,25], 63))

# print(time.clock())

print(time.clock())
print(recMc2([1,5,10,25], 63, [0]*64))

print(time.clock())