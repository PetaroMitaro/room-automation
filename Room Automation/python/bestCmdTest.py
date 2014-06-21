from winCommand import Command


file = ["what time is it","what time it","where tome is um"]
bestCmd = Command("no match found")
bestCmd.confidence=50
for key in file:
    print key
    for cmd in Command.getCommands():
        print cmd.key
        print 'best:',bestCmd.confidence
        cmd.confidence = 
