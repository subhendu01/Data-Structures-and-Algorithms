"""
Q. Write a program to print binary numbers from 1 to 10 using Queue.
Binary sequence should looks like:
1
10
11
100
101
110
111
1000
1001
1010
"""

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty.")
            return
        return self.buffer.pop()

    def is_empty(self):
        if len(self.buffer) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue('1')

    for i in range(n):
        front = numbers_queue.front()
        print("  ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()

if __name__ == "__main__":
    produce_binary_numbers(10)

