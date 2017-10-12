import sys

T = sys.stdin.readline()
for _ in range(int(T)):
    X1, Y1, X2, Y2 = sys.stdin.readline().split()
    X, Y, R = sys.stdin.readline().split()
    if int(X) - int(X1) < 0 or int(X2) - int(X) < 0 or int(Y) - int(Y1) < 0 or int(Y2) - int(Y) < 0:
        print("Don't get close to it")
        continue
    if int(X) - int(X1) < int(R) or int(X2) - int(X) < int(R) or int(Y) - int(Y1) < int(R) or int(Y2) - int(Y) < int(R):
        print("Don't get close to it")
        continue
    print('Just do it')
