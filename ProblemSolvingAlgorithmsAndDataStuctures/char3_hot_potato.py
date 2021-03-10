from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        print(simqueue.items)
        simqueue.enqueue(name)
    print(simqueue.items)
    print("----------------------")
    index = 0
    while simqueue.size() > 1:
        print("start %d loop:"%index)
        for i in range(num):
            print("*****************")
            simqueue.enqueue(simqueue.dequeue())
            print(simqueue.items)
            print("*****************")
            print("")
        simqueue.dequeue()
        index += 1
    return simqueue.dequeue()


print(hotPotato(["Bill", "D","S","J", "K", "Brad"],7))


# a = Queue()
# for i in range(6):
#     a.enqueue(i)

# print(a.items)

# a.dequeue()

# a.enqueue(a.dequeue())
# print(a.items)