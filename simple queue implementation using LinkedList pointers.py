###implementation of a queue using linked List
##Harsh Trivedi
##09/1/2018

class QueueNode():
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def enqueue(self, data):
        newqueuenode = QueueNode(data)

        if self.isEmpty():
            self.front = newqueuenode
            self.rear = newqueuenode
        else:
            self.rear.next = newqueuenode
            self.rear = newqueuenode
        

    def dequeue(self):
        if self.isEmpty():
            return float("-inf")

        else:
            popqueuenode = self.front
            self.front = self.front.next

            if self.front == None:
                self.rear = None

            return popqueuenode.data

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.dequeue()
queue.dequeue()
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print("Dequeued item is " + str(queue.dequeue()))

