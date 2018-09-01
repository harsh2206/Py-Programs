##Tom is a string freak. He has got sequences of  n words to manipulate. If in a sequence, two same words come together then he’ll destroy each other. He wants to know the number of words left in the sequence after this pairwise destruction.
## 
##
##Input:
##The first line of input contains an integer denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line of input contains an integer n denoting the number of words in a sequence. In the second line are n space separated words of the sequence. Words are contiguous stretches of printable characters delimited by white space.
## 
##
##Output:
##For each test case in a new line print the number of words left per sequence.




#Test cases
#ab aa aa bcd ab --> 3
##tom jerry jerry tom -->0

class StackNode():
    def __init__(self,data):
        self.data =data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        else:
            return self.top.data

    def push(self,data):
        newpushnode = StackNode(data)
        newpushnode.next = self.top
        self.top = newpushnode
        

    def pop(self):
        if self.isEmpty():
            return float("-inf")
        else:
            newpopnode = self.top
            self.top = self.top.next
            return newpopnode.data
            

stack = Stack()
count = 0
print("Enter the string")
line =input()
l = line.split()
for i in range(len(l)):
    if l[i] == stack.peek():
        stack.pop()
    else:
        
        stack.push(l[i])

while not stack.isEmpty():
    count+=1
    stack.pop()

print(count)
print("Yay")


    
