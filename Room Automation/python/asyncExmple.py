import asyncore, socket

class async(asyncore.dispatcher):

    def __init__(self, host, path):
        asyncore.dispatcher.__init__(self)
        print 'init'
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect( (host, 80) )
        self.i=0

    def writable(self):
        print 'check write'
        return True

    def handle_write(self):
        print 'handle write'
        sent = self.send('')

if __name__=='__main__':
    client = async('www.python.org', '/')
    asyncore.loop()
