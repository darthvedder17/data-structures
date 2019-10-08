from sys import maxsize
def create_stack():
    stack=[]
    return stack
def isempty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print(item + " pushed to stack ")
def pop(stack):
    if(isempty(stack)):
        return str(-maxsize -1)
    return stack.pop()
def peek(stack):
    if(isempty(stack)):
        return str(-maxsize -1)
    return stack[len(stack)-1]
stack=create_stack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))
print(pop(stack) + " popped from stack")
print(stack)
print(peek(stack) + " is at the top " )

