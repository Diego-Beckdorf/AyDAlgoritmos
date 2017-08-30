import sys

class Node:
    def __init__(self, string, papi):
        self.string = string
        self.papi = papi

def newNodes(v, r, black_nodes):
    new_nodes = []
    for rule in r:
        string = v.string
        l = len(string)
        i = l - len(rule[0])
        if rule[0] != string[i:]:
            continue
        new_string = string[:i] + string[i:].replace(rule[0], rule[1])
        if new_string not in black_nodes:
            new_nodes.append(Node(new_string, v))
    return new_nodes

def check_path(v):
    steps = 0
    curr_node = v
    while curr_node.papi is not None:
        steps += 1
        curr_node = curr_node.papi
    return steps

def BFS(s, t, r, case):
    black_nodes = []
    nextVertex = [Node(s, None)]
    while len(nextVertex) > 0:
        v = nextVertex.pop(0)
        if v.string == t:
            print('Case {0}: {1}'.format(case, check_path(v)))
            return True
        for node in newNodes(v, r, black_nodes):
            nextVertex.append(node)
        black_nodes.append(v)
    print('Case {0}: No Sol'.format(case))

case = 0
while True:
    stn = sys.stdin.readline().split()
    if len(stn) == 1:
        break
    case += 1
    S = stn[0]
    T = stn[1]
    N = stn[2]
    R = []
    for _ in range(int(N)):
        rule = sys.stdin.readline().split()
        R.append(rule)
    BFS(S, T, R, case)