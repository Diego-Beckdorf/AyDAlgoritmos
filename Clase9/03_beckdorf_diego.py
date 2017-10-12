import sys

class Node:
    def __init__(self,x, w):
        self.parent = self
        self.x = x
        self.w = w

    def X(self):
        return self.x

    def W(self):
        return self.w

    def Parent(self, value=None):
        if value is None:
            return self.parent
        self.parent = value

def make_set(D, node):
    if node.X() not in D:
        D[node.X()] = node

def find_root(D, x):
    if D[x].Parent() != x:
        return find_root(D, D[x].Parent())
    return x

def union(D, x, y):
    root_x = find_root(D, x)
    root_y = find_root(D, y)
    if root_x == root_y:
        return False

    if abs(x - y) >= D[x][1] + D[y][1]:
        D[x].Parent(root_y)
        return True


D = {}
n = int(sys.stdin.readline())
for _ in range(n):
    x, w = [int(i) for i in sys.stdin.readline().split()]
    node = Node(x=x, w=w)
    make_set(D, node)
