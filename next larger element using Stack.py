##Given an array A [ ] having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1 
##
##Input:
##The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. Each test case consists of two lines. The first line contains an integer N denoting the size of the array. The Second line of each test case contains N space separated positive integers denoting the values/elements in the array A[ ].
## 
##Output:
##For each test case, print in a new line, the next greater element for each array element separated by space in order.
##

##1<=A[i]<=1000
##
##Example:
##Input
##1
##4
##1 3 2 4 
##
##Output
##3 4 4 -1
##
##Explanation
##In the array, the next larger element to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? since it doesn't exist hence -1.
##
##** For More Input/Output Examples Use 'Expected Output' option **



class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
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
        self.top =newpushnode

    def pop(self):
        if self.isEmpty():
            return float("-inf")
        else:
            newpopnode = self.top
            self.top = self.top.next
            return newpopnode.data

stack = Stack()

k=[]
m=[]
print("Enter the array input seperated by comma:")
a = input()
a = a.split(',')
a = list(map(int, a))
for i in range(len(a)):
    if a[i]==max(a):
        stack.push("-1")
        continue
    else:
        if i==0:
            for j in range(i+1,len(a)):
                if a[j]>a[i]:
                    stack.push(a[j])
                    break
        else:
            k=a[i+1::1]
            m=a[i-1::-1]
            for x in range(len(k)):
                if k[x]>a[i]:
                    
                    break
            for y in range(len(m)):
                if m[y]>a[i]:
                    
                    break


            if x==y:
                if k[x]>m[y]:
                    stack.push(k[x])
                else:
                    stack.push(m[y])
            elif x<y and k[x]>a[i]:
                stack.push(k[x])
            elif y<x and m[y]>a[i]:
                stack.push(m[y])
            else:
                stack.push(max(k[x],m[y]))


stackfinal = Stack()
for i in range(len(a)):
    stackfinal.push(stack.pop()) 
for i in range(len(a)):
    print(str(a[i])+'-->'+str(stackfinal.pop()))


print("Yay!")

    

##input -> 1,3,2,4
##output -> 3,4,4,-1
    
            
                
        
    
        
        




    
        
    

    
        
        
