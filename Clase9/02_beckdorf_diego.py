import sys


def find(stack, val):
    i_S = []
    for i, n in reversed(list(enumerate(stack))):
        if n[:2] == val:
            i_S.append(i)
    for i in i_S:
        stack.pop(i)
    if len(i_S) > 0:
        return True
    return False


def clean(stack, t, d):
    i = []
    for j, n in list(enumerate(stack)):
        if t - int(n[2]) > d:
            i.append(j)
    for j in i:
        stack.pop(j)


pairs_if_friends = []
stack = []
line = sys.stdin.readline().split()
n = line[0]
d = int(line[1])
for _ in range(int(n)):
    line = sys.stdin.readline().split()
    t = int(line[2])
    clean(stack, t, d)
    val = [line[1], line[0]]
    if val in pairs_if_friends or reversed(val) in pairs_if_friends:
        continue
    if find(stack, val):
        if line[:2] not in pairs_if_friends or val not in pairs_if_friends:
            pairs_if_friends.append(val)
    else:
        stack.append(line)

print(len(pairs_if_friends))
for pair in pairs_if_friends:
    print(' '.join(pair))
