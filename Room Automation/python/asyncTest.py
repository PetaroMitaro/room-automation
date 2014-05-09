import Queue
import threading

def f(q):
    q.put('put data to thread')

if __name__ == '__main__':
    q = Queue.Queue()
    t = threading.Thread(target=f, args=(q,))
    t.daemon = True
    t.start()
    q.get()
    
