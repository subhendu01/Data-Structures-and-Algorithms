# When more than key point to same one address
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        found = False
        for idx, ele in enumerate(self.arr[h]):
            if len(ele) == 2 and ele[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
        if found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, ele in enumerate(self.arr[h]):
            if ele[0] == key:
                del self.arr[h][idx]
        # self.arr[h] = None
hash = HashTable()

hash.get_hash('march 7')
print(hash.__delitem__('march 7'))