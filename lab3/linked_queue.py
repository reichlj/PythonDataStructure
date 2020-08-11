### File: linked_queue.py
from lab3.node import Node
import time

class LinkedQueue(object):
    def __init__(self):
        self._front = None
        self._size = 0
        self._rear = None

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = node
            self._rear = node
        else:
            self._rear.setNext(node)
            self._rear = node
        self._size = self._size + 1

    def dequeue(self):
        current = self._front
        if self._size == 1:
            self._front = None
            self._rear = None
        else:
            self._front = current.getNext()
        self._size = self._size - 1
        return current.getData()

    def peek(self):
        return self._front.getData()

    def size(self):
        return self._size

    def __str__(self):
        resultStr = ""
        temp = self._front
        while temp != None:
            resultStr += str(temp.getData()) + " "
            temp = temp.getNext()
        resultStr = "(front) " + resultStr + "(rear)"
        return resultStr
    
        
if __name__ == "__main__":
    qt = LinkedQueue()
    for k in range(4):
        qt.enqueue(k)
        print(qt)
    for k in range(4):
        print(qt.dequeue())
        print(qt)

    n = 1000
    for i in range(7):
        n = n*2
        qt = LinkedQueue()
        start = time.time()
        for k in range(n):
            qt.enqueue(k)
        enq_time = time.time() - start
        start = time.time()
        for k in range(n):
            qt.dequeue()
        deq_time = time.time() - start
        print("n={0:7d} enqueue: {1:10.6f} dequeue: {2:10.6f} size: {3}".format(
              n, enq_time,deq_time,qt._size))
    n=1000
    for i in range(3):
        n = n*10
        qt = LinkedQueue()
        start = time.time()
        for k in range(n):
            qt.enqueue(k)
        enq_time = time.time() - start
        start = time.time()
        for k in range(n):
            qt.dequeue()
        deq_time = time.time() - start
        print("n={0:7d} enqueue: {1:10.6f} dequeue: {2:10.6f} size: {3}".format(
              n, enq_time,deq_time,qt._size))
