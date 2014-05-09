from time import sleep

class texter:

    
    def __init__(self):
        #probably gonna use send grid API
        self.foo = 'bar'

def checkInbox(queue):
    for i in range(15):
        sleep(0.2)
        queue.put("found a text")
