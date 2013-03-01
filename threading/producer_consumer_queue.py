"""
Multi Threading example to show a common Producer/Consumer paradigm.
"""
import threading
import Queue


class Producer(threading.Thread):
    """
    Producer class that takes the raw data and performs some work on it.
    Once this work is complete it puts the resultant data in to the out queue
    for the Consumer class.
    """
    def __init__(self, in_queue, out_queue):
        threading.Thread.__init__(self)
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        while True:
            #grab the data from the in queue
            item = self.in_queue.get()

            #here we should do some work with item
            #and then put the new data in the out queue
            result = 'You should be doing work.'
            self.out_queue.put(result)

            #signal that the worker task is done
            self.in_queue.task_done()

class Consumer(threading.Thread):
    """
    Consumer class that takes the data outputted by the Producer class and
    consumes the data from the out queue and outputs a meaningful result.
    """
    def __init__(self, out_queue):
        threading.Thread.__init__(self)
        self.out_queue = out_queue

    def run(self):
        while True:
            #grab the data from the out queue
            item = self.out_queue.get()

            #here we should consume the item and
            #turn it in to whatever output we desire
            result = 'This is your awesome output.'

            #signal that the consumer task is done
            self.out_queue.task_done()

if __name__ == '__main__':

    #Create the queues and list to be used
    item_list = ['item1', 'item2', 'item3']
    in_queue = Queue.Queue()
    out_queue = Queue.Queue()

    #spawn our producer threads and start work
    for i in xrange(len(item_list)):
       t = Producer(in_queue, out_queue)
       t.daemon = True
       t.start()

    #put the items in queue
    for item in item_list:
        in_queue.put(item)


    #spawn our consumer threads and start consuming
    for i in xrange(len(item_list)):
        t = Consumer(out_queue)
        t.daemon = True
        t.start()

    #now block until all data has been processed in
    #both queues
    in_queue.join()
    out_queue.join()
