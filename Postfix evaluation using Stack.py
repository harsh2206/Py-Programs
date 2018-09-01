##Evaluate a postfix expression 
#Create by : Harsh Trivedi
#Date 08/25/2018

#Test case  231*+9- --> ((2+(3*1))-9)  --> -4



class StackNode():
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top  = None

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self,data):
        newpushednode = StackNode(data)
        newpushednode.next = self.top
        self.top = newpushednode

    def pop(self):
        if self.isEmpty():
            return float("-inf")
        else:
            newpopednode = self.top
            self.top = self.top.next
            return newpopednode.data

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        else:
            return self.top.data


def evaluate(c1,c2,char):
    if char == '+':
        return c1+c2
    elif char == '-':
        return c1-c2
    elif char == '*':
        return c1*c2
    elif char == '/':
        return c1/c2
    else:
        return None
        

print("Enter a postfix expression that needs to be evaluated")
st = str(input())
stack = Stack()
for char in st:
    if char.isdigit():
        stack.push(char)
    elif char in ('+', '-','*','/'):
        c2 = stack.pop()
        c1 = stack.pop()
        stack.push(evaluate(int(c1),int(c2),char))
    else:
        print("Invalid Symbol found")

print("Final evaluated value =" + str(stack.pop()))




        
