import sys
import math
from collections import defaultdict


class Vertex:
    def __init__(self, n):
        self.n = n
        self.dist = math.inf
        self.parent = None
        self.lenght = 0
        self.c1 = None
        self.c2 = None


def menor(L):
    closer = Vertex(n=-1)
    for u in L:
        if u.dist < closer.dist:
            closer = u
    return closer


def adj(V, E, u):
    R = []
    for v in E[u.n]:
        for w in V:
            if w.n == v:
                yield w


def getDistance(v1, v2, D):
    if (v1.n, v2.n) in D:
        return D[(v1.n, v2.n)]
    else:
        return D[(v2.n, v1.n)]


def showRoute(V):
    t = None
    for v in V:
        if v.n == 1:
            t = v
    route = [t.dist]
    while t.parent is not None:
        route = [t.n] + route
        t = t.parent
    print(' '.join(str(c) for c in [0] + route))


def checkNewState(u, v, D):
    d = getDistance(u, v, D)
    if u.lenght > 2:
        if d > u.c1:
            u.c1 = d
        elif d > u.c2:
            u.c2 = d
        else:
            pass
    elif u.lenght == 2:
        c1, c2 = 0
        curr = u
        while curr.parent is not None:
            d2 = getDistance(curr, curr.parent, D)
            if d2 > c1:

                c1 = d2
            if d2 > d and d2 > c2:
                c2 = d2
    elif u.lenght == 1:
        d2 = getDistance(u, u.parent, D)
        if d > d2:
            v.c1 = d
        else:
            v.c1 = d2
    if v.dist > u.dist + d:
        v.dist = u.dist + d
        v.parent = u


def Dijkstra(D, E, n):
    # D es un diccionario con las distancias entre (v1, v2)
    # E es representación por matriz de adyacencia como diccionario de listas
    # n es la cantidad de ciudades sin considerar 0 y 1

    V = [Vertex(n=0), Vertex(n=1)]
    for _ in range(n):
        V.append(Vertex(n=len(V)-1))
    checked = []
    V[0].dist = 0

    while len(V) > 0:
        u = menor(V)
        V.remove(u)
        for v in adj(V, E, u):
            d = getDistance(u, v, D)
            if v.dist > u.dist + d:
                v.dist = u.dist + d
                v.parent = u
        checked.append(u)
    showRoute(checked)


while True:
    N = sys.stdin.readline()
    if N.strip() == "0":
        break
    E = defaultdict(list)
    D = {}
    n = 1
    for _ in range(int(N)):
        s, e, c = sys.stdin.readline().split()
        s = int(s)
        e = int(e)
        c = int(c)
        if (s, e) not in D:
            D[(s, e)] = c
            E[s].append(e)
            E[e].append(s)
    Dijkstra(D=D, E=E, n=max(E.keys()))
