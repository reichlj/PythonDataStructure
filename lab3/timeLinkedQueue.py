from lab3.linked_queue import LinkedQueue
import time

def main():
    n = 100000
    myQueue = LinkedQueue()
    start = time.clock()
    for count in range(n):
        myQueue.enqueue(count)

    end = time.clock()
    print("Time to enqueue",n, "items to a LinkedQueue was %.9f seconds" % (end-start))

    start = time.clock()
    for count in range(n):
        temp = myQueue.dequeue()

    end = time.clock()
    print("Time to dequeue",n, "items to a LinkedQueue was %.9f seconds" % (end-start))

main()
input("Hit Enter to continue")
