""" File: sorted_list_priority_queue.py
    Description:  Priority queue implemented using a Python list ordered by
    priority in descending order.
"""


class SortedListPriorityQueue:
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        testIndex = len(self._items) - 1
        self._items.append(item)
        while testIndex >= 0 and item >= self._items[testIndex]:
            self._items[testIndex + 1] = self._items[testIndex]
            testIndex -= 1
        self._items[testIndex+1] = item

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        currentIndex = len(self._items) - 1
        while currentIndex >= 0:
            yield self._items[currentIndex]
            currentIndex -= 1
        raise StopIteration
        
if __name__ == '__main__':
    q = SortedListPriorityQueue()
    print("q.enqueue(5)")
    q.enqueue(5)
    print("q.enqueue(7)")
    q.enqueue(7)
    print("q.enqueue(3)")
    q.enqueue(3)
    print("q.enqueue(4)")
    q.enqueue(4)
    print("q.enqueue(1)")
    q.enqueue(1)
    print("q.enqueue(9)")
    q.enqueue(9)
    print(q)
    print("q.dequeue():",q.dequeue())
    print("q:",q)
    for item in q:
        print(item)
        

    
    
    
