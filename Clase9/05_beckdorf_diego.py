import sys

def push(stack, n):
    stack.append(n)

def pop(stack, operation):
    x1 = stack.pop()
    x2 = stack.pop()
    result = x1 + x2 if operation == '+' else x1 * x2
    push(stack, result)

string = sys.stdin.readline().strip()
stack = []

for char in string:
    if char in ['+', '*']:
        pop(stack, char)
    else:
        push(stack, int(char))
print(stack.pop())