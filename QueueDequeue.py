# implementation of queue and dequeue FIFO(First in First out)

class Queue:
    def __init__(self):
        self.queue = []

    def queue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if len(self.queue):
            self.queue.remove(self.queue[0])
        else:
            return None

    def peek(self):
        if len(self.queue):
            return self.queue[0]
        else:
            return None

    def __str__(self):
        return str(self.queue)


my_queue = Queue()
my_queue.queue(23)
my_queue.queue(3)
my_queue.queue(25)
my_queue.queue(2)
print(my_queue)
my_queue.dequeue()
print(my_queue)
print(my_queue.peek())
