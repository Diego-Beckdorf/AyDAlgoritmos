import sys


def new_nodes(node, n, l):
    nodes = []
    for c_n in range(1, l+1):
        new_node = node[::]
        dif_n = new_node[-1]
        new_node.pop(-1)
        dif = c_n - dif_n
        new_node += [c_n, dif]
        nodes.append(new_node)
    return nodes



def noob_mage(n, d, l):
    nodes = [[d]]
    while len(nodes) != 0:
        node = nodes[0]
        nodes.pop(0)
        if len(node[:-1]) == n:
            if node[-1] == 0:
                return ' '.join([str(i) for i in node[:-1]])
            continue
        nodes += new_nodes(node, n, l)
    return -1

T = sys.stdin.readline().split()
n = int(T[0])
d = int(T[1])
l = int(T[2])
print(noob_mage(n, d, l))