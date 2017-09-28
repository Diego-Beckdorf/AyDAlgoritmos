import sys

def find_nadia(article):
    nadia = 'nadia'
    i = 0
    for j in article:
        if j == nadia[i]:
            i += 1
            if i == 5:
                return 'YES'
    return 'NO'

T = sys.stdin.readline()
for _ in range(int(T)):
    article = sys.stdin.readline()
    print(find_nadia(article))