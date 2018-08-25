#Create a stack using Linked List and check if the paranthesis is balanaced or not?????

#for example ({[]}) is balanced but [{)]{ is not

# Program created by Harsh Trivedi
# Date: 08/25/2018

class StackNode():
    def __init__(self,data):
        self.data = data
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
        newpushednode = StackNode(data)
        newpushednode.next = self.top
        self.top = newpushednode
##        print("%s - is added to the stack. Cheers!"%data)

    def pop(self):
        if self.isEmpty():
            return float("-inf")
        else:
            newpopnode = self.top
            self.top = self.top.next
            newpopdata = newpopnode.data
            return newpopdata

##stack = Stack()
##stack.push(10)
##stack.push("I will learn programming")
##stack.push("Stack successfully implemented")
##stack.pop()
##print("Current top element:"+ str(stack.peek()))
##stack.pop()

def balancedparanthesis():
    
    print("Enter Data please")
    exp = input()
    stack = Stack()

    for character in exp:
        if character in ('(','{','['):
            stack.push(character)
            continue

    
        if character in (')','}',']'):

            if character == '}' and stack.pop() == '{':
                continue
    
            elif character == ']' and stack.pop() == '[':
                continue
            elif character == ')' and stack.pop() == '(':
                continue
            else:
                print("paranthesis not matching")
                return False
       
    if stack.isEmpty():
        return True
    else:
        return False

print(balancedparanthesis())














        
