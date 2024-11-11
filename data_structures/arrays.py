class Array:
    def __init__(self, size):
        self.size = size
        self.length = 0
        self.A = [None] * size

    def display(self):
        for i in range(self.length):
            print(self.A[i], end=" ")
        print()

    def append(self, x):
        if self.length < self.size:
            self.A[self.length] = x
            self.length += 1
        else:
            print("Array is full")

    def insert(self, index, x):
        if index >= 0 and index <= self.length:
            for i in range(self.length, index, -1):
                self.A[i] = self.A[i - 1]
            self.A[index] = x
            self.length += 1
        else:
            print("Invalid Index")

    def delete(self, index):
        if index >= 0 and index < self.length:
            x = self.A[index]
            for i in range(index, self.length - 1):
                self.A[i] = self.A[i + 1]
            self.length -= 1
            return x
        else:
            return -1

    def linear_search(self, key):
        """
        Performs linear search to find the index of the given key.

        Time complexity: O(N)
        Space complexity: O(1)
        """
        for i in range(self.length):
            if self.A[i] == key:
                return i
        return -1

if __name__ == "__main__":
    arr = Array(10)

    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.insert(2, 15)
    arr.display()

    print(arr.delete(2))
    arr.display()

    print(arr.linear_search(20))