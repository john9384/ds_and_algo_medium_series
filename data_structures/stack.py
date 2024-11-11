class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        Pushes an item onto the top of the stack.

        Time complexity: O(1)
        Space complexity: O(N)
        """
        self.stack.append(item)

    def pop(self):
        """
        Removes and returns the item at the top of the stack.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        """
        Checks if the stack is empty.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return len(self.stack) == 0