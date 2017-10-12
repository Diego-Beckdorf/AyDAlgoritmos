import sys

def cross_product(O, P, Q):
    return ((P[0] - O[0])*(Q[1] - O[1]) - (P[1] - O[1])*(Q[0] - O[0]))

def is_inside(Triangle, P):
    for i in range(len(Triangle)):
        cp = cross_product(P, Triangle[i], Triangle[(i+1)%3])
        if cp > 0:
            return False
    return True

n = int(sys.stdin.readline())
Poligon = []
for v in range(n):
    Poligon.append([int(i) for i in sys.stdin.readline().split()])
t = sys.stdin.readline()
for _ in range(int(t)):
    count = 0
    P = [int(i) for i in sys.stdin.readline().split()]
    for v1 in range(n):
        for v2 in range(v1, n):
            if v2 == v1:
                continue
            for v3 in range(v2, n):
                if v3 == v1 or v3 == v2:
                    continue
                Triangle = [Poligon[v1], Poligon[v2], Poligon[v3]]
                if is_inside(Triangle=Triangle, P=P):
                    count += 1
    print(count)
