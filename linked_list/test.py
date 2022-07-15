class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove(self, val):
        if self.head is None:
            return
        if self.head.data == val:
            self.head = self.head.next
            return

        itr = self.head
        while itr:
            print(itr.data)
            # if itr.next.data == val:
            #     itr.next = itr.next.next
            itr = itr.next
        return str(val) + "deleted"

    def find_particular_element(self):
        d = {}
        itr = self.head

        while itr:
            count = 0
            if itr.data == itr.next:
                d[itr.data] = count
            itr = itr.next
        return d

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        while itr:
            print(itr.data, end=' ')
            itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_end(12)
    ll.insert_beginning(15)
    # ll.insert_beginning(14)
    # ll.insert_beginning(16)

    ll.remove(12)
    ll.print()
    print("\n")

    # print(ll.find_particular_element())



