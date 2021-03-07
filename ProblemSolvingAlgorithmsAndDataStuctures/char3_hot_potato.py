from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        print(simqueue.items)
        simqueue.enqueue(name)
    print(simqueue.items)
    print("----------------------")
    while simqueue.size() > 1:
        for i in range(num):
            print("*****************")
            simqueue.enqueue(simqueue.dequeue())
            print(simqueue.items)
            print("*****************")

        simqueue.dequeue()
        print("~~~~~~~~~~~~~~~~")
        print(simqueue.items)
        print("~~~~~~~~~~~~~~~")
    return simqueue.dequeue()


print(hotPotato(["jack", "jo","pan","kent"],4))
