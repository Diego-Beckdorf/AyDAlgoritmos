import sys


def es_solucion(N, H, s):
    if len(s) != N:
        return False
    if sum(int(c) for c in s) != H:
        return False
    return True


def siguiente_solucion(s, N):
    if len(s) < N:
        for c in ['0', '1']:
            yield c + s


def backtracking(N, H, s=''):
    if es_solucion(N, H, s):
        print(s)
    else:
        for s_a in siguiente_solucion(s, N):
            backtracking(N, H, s_a)


def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * factorial(N-1)

M = int(sys.stdin.readline())

for _ in range(M):
    N, H = tuple(sys.stdin.readline().split())
    N = int(N)
    H = int(H)
    backtracking(N, H)
