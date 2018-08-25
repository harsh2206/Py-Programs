##Reverse a string using Stack (Linked List)

#Created by Harsh Trivedi
#Date : 08/25/2018

class StackNode():
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None

    def isEmpty(self):
        if self.top ==None:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        else:
            return self.top.data

    def push(self,data):
        newpushednode = StackNode(data)
        newpushednode.next = self.top
        self.top = newpushednode
##        print(newpushednode.data)

    def pop(self):
        if self.isEmpty():
            return float("-inf")
        else:
            newpopednode = self.top
            self.top = self.top.next
            return newpopednode.data


print("Enter a string required to perform reverse operation")
str = input()
stack = Stack()
rev = []
for character in str:
    stack.push(character)

for i in range(len(str)):
    rev.append(stack.pop())

for revchar in rev:
    print(revchar)
