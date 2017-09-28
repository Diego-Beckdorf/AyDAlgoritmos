import sys
import math


def get_row(h):
    return h // 8 + 1


def get_col(h):
    return h % 8 if h % 8 != 0 else 8


class Node:
    def __init__(self, h, ps, horse_moves=0, status=None, parent=None):
        self.parent = parent
        self.h = h
        self.ps = ps
        self.horse_moves = horse_moves
        self.status = status

    def new_horse_positions(self):
        moves = [-17, -15, -10, -6, 6, 10, 15, 17]
        row = get_row(self.h)
        col = get_col(self.h)
        Hi = []
        for move in moves:
            h = self.h + move
            if h < 1 or h > 64:
                continue
            hrow = get_row(h)
            hcol = get_col(h)
            if abs(row - hrow) > 2 or abs(col - hcol) > 2:
                continue
            Hi.append(h)
        return Hi

    def move_powns(self):
        new_ps = []
        for pown in self.ps:
            if pown + 8 == self.h:
                self.status = 'perdio'
            new_ps.append(pown + 8)
            if max(new_ps) > 64:
                self.status = 'perdio'
        self.ps = new_ps

    def new_nodes(self):
        new_nodes = []
        new_horse_positions = self.new_horse_positions()
        for horse_position in new_horse_positions:
            new_ps = self.ps[::]
            if horse_position in new_ps:
                new_ps.remove(horse_position)
            status = 'gano' if len(new_ps) == 0 else self.status
            new_nodes.append(Node(h=horse_position, ps=new_ps,
                                  horse_moves=self.horse_moves + 1,
                                  status=status, parent=self))
        for new_node in new_nodes:
            new_node.move_powns()
        return new_nodes


def backtracking(node):
    min = math.inf
    if node.status == 'perdio':
        return False
    if node.status == 'gano':
        return node.horse_moves
    valid_nodes = node.new_nodes()
    for n in valid_nodes:
        val = backtracking(n)
        if not val:
            continue
        if val < min:
            min = val
    return min

T = None
while True:
    T = sys.stdin.readline()
    if T == '0':
        break
    T_vals = T.split()
    p = int(T_vals[0])
    AP = []
    for i in range(1, p + 1):
        AP.append(int(T_vals[i]))
    H = int(T_vals[-1])
    root = Node(h=H, ps=AP)
    val = backtracking(root)
    if val == math.inf:
        print('impossible')
    else:
        print(val)