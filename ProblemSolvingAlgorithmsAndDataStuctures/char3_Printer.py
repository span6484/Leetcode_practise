from pythonds.basic import Queue
import random


class Printer:

    def __init__ (self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0


    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        
        else:
            return False


    def startNext(self, newtask):
        self.currentTask = newtask

        self.timeRemaining = newtask.getPages() * 60/ self.pagerate




class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    

    def waitime(self, currenttime):
        return currenttime - self.timestamp


def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagePerMinute):
    labprinter = Printer(pagePerMinute)
    printQueue = Queue()
    waitingTime = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingTime.append(nexttask.waitime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    
    averageWait = sum(waitingTime) / len(waitingTime)
    print("Average Wait %6.2f sec %3d tasks remaining. " % (averageWait, printQueue.size()))




for i in range(10):
    simulation(3600, 5)
        






