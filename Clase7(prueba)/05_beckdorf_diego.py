import sys
import math


def get_row(h):
    return h // 8 + 1


def get_col(h):
    return h % 8 if h % 8 != 0 else 8


class Node:
    def __init__(self, knight_position, blocked, knight_moves=0, parent=None, known_positions=[]):
        self.parent = parent
        self.knight_position = knight_position
        self.blocked = blocked
        self.knight_moves = knight_moves
        self.known_positions = known_positions

    def new_knight_positions(self):
        moves = [-17, -15, -10, -6, 6, 10, 15, 17]
        row = get_row(self.knight_position)
        col = get_col(self.knight_position)
        new_knight_positions = []
        for move in moves:
            new_knight_position = self.knight_position + move
            if new_knight_position in self.known_positions:
                continue
            if new_knight_position in self.blocked:
                continue
            if new_knight_position < 1 or new_knight_position > 64:
                continue
            hrow = get_row(new_knight_position)
            hcol = get_col(new_knight_position)
            if abs(row - hrow) > 2 or abs(col - hcol) > 2:
                continue
            new_knight_positions.append(new_knight_position)
        return new_knight_positions

    def new_nodes(self):
        new_nodes = []
        new_knight_positions = self.new_knight_positions()
        for new_knight_position in new_knight_positions:
            new_nodes.append(Node(knight_position=new_knight_position,
                                  blocked=self.blocked,
                                  knight_moves=self.knight_moves + 1,
                                  parent=self,
                                  known_positions=self.known_positions + [new_knight_position]))
        return new_nodes


FIN = None

def BFS(root):
    queue = [root]
    while len(queue) > 0:
        node = queue[0]
        queue.pop(0)
        if node.knight_position == FIN:
            return node.knight_moves
        queue += node.new_nodes()


def cook_position(p):
    col = 'abcdefgh'
    return col.index(p[0])*8 + int(p[1])
    

b = None
board = 0
while True:
    b = sys.stdin.readline()
    if int(b) == -1:
        break
    board += 1
    if int(b) > 0 :
        blocked = [cook_position(p) for p in sys.stdin.readline().split()]
    start_end = sys.stdin.readline().split()
    knight_position = cook_position(start_end[0])
    FIN = cook_position(start_end[1])
    root = Node(knight_position=knight_position, blocked=blocked)
    val = BFS(root)
    output = '{0} moves'.format(val) if val is not None else 'not reachable'
    print('Board {0}: {1}'.format(board, output))