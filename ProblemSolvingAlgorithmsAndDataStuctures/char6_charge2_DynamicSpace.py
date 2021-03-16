def dpMakeChange(coinValueList, change, minCoins):
    #从1分开始到change逐个计算最少硬币数
    for cents in range(1, change + 1):
        # 初始化一个最大值
        coinCount = cents
        # 减去每个硬币，向后查找最少硬币数，记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            print("c is {}".format(c))
            print("j is {}".format(j))
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        
        # 得到当前最少硬币数， 记录
        minCoins[cents] = coinCount
    
    return minCoins[change]


print(dpMakeChange([1,5,10,21,25], 63, [0]*64))
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_281.jdk/Contents/Home