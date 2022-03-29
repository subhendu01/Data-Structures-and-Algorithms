class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None]*self.MAX

    def get_hash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
hash = HashTable()

hash.get_hash('march 7')
print(hash.__delitem__('march 7'))