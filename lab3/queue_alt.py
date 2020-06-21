### File: queue_alt.py
import time
class QueueAlt:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        resultStr = "(front)"
        for item in self.items:
            resultStr = resultStr + " " + str(item)
        resultStr = resultStr + " (rear)"
        return resultStr
    
if __name__ == "__main__":
    n = 1000
    for i in range(7):
        n = n*2
        qt = QueueAlt()
        start = time.time()
        for k in range(n):
            qt.enqueue(k)
        enq_time = time.time() - start
        start = time.time()
        for k in range(n):
            qt.dequeue()
        deq_time = time.time() - start
        print("n={0:7d} enqueue: {1:10.6f} dequeue: {2:10.6f}".format(
              n, enq_time,deq_time))
    n=1
    for i in range(5):
        n = n*10
        qt = QueueAlt()
        start = time.time()
        for k in range(n):
            qt.enqueue(k)
        enq_time = time.time() - start
        start = time.time()
        for k in range(n):
            qt.dequeue()
        deq_time = time.time() - start
        print("n={0:7d} enqueue: {1:10.6f} dequeue: {2:10.6f}".format(
              n, enq_time,deq_time))

