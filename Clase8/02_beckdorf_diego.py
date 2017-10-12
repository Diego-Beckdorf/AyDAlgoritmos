import sys

def cross_product(P, Q):
    return (P[0]*Q[1] - P[1]*Q[0])

N = sys.stdin.readline()
wonejos = []
for _ in range(int(N)):
    wonejos.append([int(i) for i in sys.stdin.readline().split()])

max = 0
for i in range(len(wonejos)):
    P = wonejos[i]
    for j in range(len(wonejos)):
        if i == j:
            continue
        count = 2
        Q = wonejos[j]
        m = (P[1] - Q[1]) / (P[0] - Q[0])
        n = P[1] - m * P[0]
        for k in range(len(wonejos)):
            if k == i or k == j:
                continue
            R = wonejos[k]
            if R[1] == m*R[0] + n:
                count += 1
    if count > max:
        max = count
print(max)
