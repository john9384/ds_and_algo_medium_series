class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """
        Adds an item to the rear of the queue.

        Time complexity: O(1)
        Space complexity: O(N)
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        """
        Checks if the queue is empty.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return len(self.queue) == 0