# #
# # ! Using list
# que = []
# que.append("1")
# que.append("2")
# que.append("3")

# print(que)

# que.pop(0)
# que.pop(0)
# que.pop(0)

# print(que)

# #! Using class


class Queue:
    def __init__(self):
        self.queue = list()

    # Add item
    def enqueue(self, val):
        if val not in self.queue:
            self.queue.append(val)
            return True
        return False

    # Remove item
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    # Return size
    def size(self):
        return len(self.queue)

    # isEmpty
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

    # Print queue
    def getQueue(self):
        return self.queue


myque = Queue()
myque.enqueue(1)
myque.enqueue(2)
myque.enqueue(3)

print(myque.size())

print(myque.getQueue())

myque.dequeue()
# myque.dequeue()
# myque.dequeue()

print(myque.isEmpty())

print(myque.getQueue())
