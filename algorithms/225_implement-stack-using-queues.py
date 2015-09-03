class Queue(object):
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if len(self.queue) == 0:
            return -1
        firstElement = self.queue[0]
        self.queue = self.queue[1:]
        return firstElement

    def top(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """ 
        self.queue.push(x)
        for i in range(len(self.queue.queue)-1):
            self.queue.push(self.queue.pop())

    def pop(self):
        """
        :rtype: nothing
        """ 
        return self.queue.pop()

    def top(self):
        """
        :rtype: int
        """ 
        return self.queue.top()

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue.empty()

if __name__ == "__main__":
    stack = Stack()
    
    print("Pushing 1, 2, 3, 4")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print("Now stack is : " + str(stack.queue.queue))
    
    print("Popping one time")
    print(stack.pop())
    print("Now stack is : " + str(stack.queue.queue))

    print("Getting top ")
    print(stack.top())

    print("Now stack is : " + str(stack.queue.queue))

    print("Is stack empty?")
    print(stack.empty())