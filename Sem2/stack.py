#
# ! Implement stack using collection module
from collections import deque

stack = deque()

stack.append("a")
stack.append("b")
stack.append("c")

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)

# ! Using list
myStack = []

myStack.append("a")
myStack.append("ab")
myStack.append("abc")

print(myStack)

print(myStack.pop())
print(myStack.pop())
print(myStack.pop())

print(myStack)
