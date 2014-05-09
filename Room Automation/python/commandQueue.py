#The prupose of the command queue is to hold commands
#In the event that more than one command comes in at once, this will keep a stack
#that way while one command is being executed, another can be issued
class commandQueue:

    def __init__(self,maxSize):
        self.queue=[]
        #start command ID numbers at 0
        self.ID=0
        self.maxSize=maxSize        

    #add command
    def add(self,c):
        #for each new command increment ID number
        self.ID+=1
        #tag new command and add to list
        c.setID(self.ID)
        self.queue.append(c)

    #get next ID so that each command is uniquely identified
    

class command:

    #constructor
    def __init__(self,text):
        self.text=text
        self.completed=False
        self.ID=0

    #execute the command
    def execute():
        print 'executing command'
        self.completed=true

    def setID(ID):
        self.ID=ID
        
