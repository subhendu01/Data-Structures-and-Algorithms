import threading
import time
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

q = Queue()

def place_orders(orders):
    for order in orders:
        print('Place order')
        q.enqueue(order)
        time.sleep(0.5)

def serve_orders():
    time.sleep(1)
    while True:
        q.dequeue()
        print('Now order serving')
        time.sleep(2)

if __name__ == "__main__":
    orders = ['pizza', 'biriyani', 'chicken']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()