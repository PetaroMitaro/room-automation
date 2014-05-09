from multiprocessing import Process,Queue
import commandQueue
import recordCommand
import texter
from threading import Thread

KEYWORD='Sherlock'

class automator:

    def __init__(self,keyword):
        print "Initiating Room Automation System"
        #store keyword 
        self.keyword=keyword
        #setup queue
        self.threadQueue = Queue()
        #create threads
        texterThread=Thread(target=texter.checkInbox, args=(self.threadQueue,))
        audioThread=Thread(target=recordCommand.recordCommand, args=(self.threadQueue,))
        #set to backround tasks
        texterThread.daemon = True
        audioThread.daemon = True
        #start threads 
        texterThread.start()
        audioThread.start()


    def run(self):
        #scan for commands
        while True:
            #read in all waiting commands from queue
            while not self.threadQueue.empty():
                #move from thread queue to command queue
                self.commandQueue.add(self.threadQueue.get())
            for c in self.commandQueue:
                c.execute()
            
        
        
if __name__ == '__main__':
    auto = automator(KEYWORD)
    auto.run()
    
