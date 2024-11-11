class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """
        A simple hash function.
        
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.

        Time complexity: O(1) on average, O(n) in the worst case (if many collisions occur)
        Space complexity: O(n)
        """
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        """
        Searches for a value associated with a given key.

        Time complexity: O(1) on average, O(n) in the worst case (if many collisions occur)
        Space complexity: O(1)
        """
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table.

        Time complexity: O(1) on average, O(n) in the worst case (if many collisions occur)
        Space complexity: O(1)
        """
        index = self.hash_function(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                self.table[index].pop(i)
                break