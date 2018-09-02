###implementation of a circular queue using array
##Harsh Trivedi
##09/1/2018

class CircularQueue:
    def __init__(self, maxSize):
        self.queue = list()
        self.maxSize = maxSize
        self.front = -1
        self.tail = -1
        self.queue = [None]*maxSize

    def enqueue(self, data):
        
        if (self.front == 0 and self.tail == self.maxSize-1) or (self.tail == self.front-1):   ##condition for queue is full
            print("Queue Full")
        elif self.front == -1 and self.tail == -1:  # condition when queue is completely empty
            self.front = self.tail = 0
            
            self.queue[self.tail] = data
        elif self.front != 0 and self.tail == self.maxSize-1:   # condition when queue is not full but tail is pointing maxsize
            self.tail = 0
            self.queue[self.tail] = data
        
        else:                              # condition when queue is not full and tail is yet to reach maxsize
            self.tail +=1
            self.queue[self.tail]=data

    def dequeue(self):
        if self.front == -1:
            self.tail = -1
            print("Queue Empty")
        elif self.front==self.tail:
            print(self.queue[self.front])
            self.queue[self.front] = None

            self.front = -1
            self.tail = -1
        elif self.front ==self.maxSize - 1:
            print(self.queue[self.front])
            self.queue[self.front] = None
            self.front = 0
        else:
            print(self.queue[self.front])
            self.queue[self.front] = None
            self.front +=1

            
        
        
    
size = input("Enter the size of the Circular Queue")
q = CircularQueue(int(size))


q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue('Study')
q.enqueue(70)
q.dequeue()
q.enqueue(80)

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(90)
q.dequeue()
q.enqueue(100)
q.enqueue(110)
q.dequeue()
q.dequeue()
q.dequeue()


##you can debug the value in the index using the command q.queue on the python interpreter







