class Stack(object):

    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def pop(self):
        if self.item == []:
            return None
        else:
            return self.item.pop()

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.item == []

def reverse(str):
    rev_str = ''
    stack = Stack()

    for i in range(len(str)):
        stack.push(str[i])

    while not stack.isEmpty():
        temp = stack.pop()
        rev_str = rev_str + temp

    return rev_str

if __name__ == "__main__":
    print(reverse("Subhendu"))

