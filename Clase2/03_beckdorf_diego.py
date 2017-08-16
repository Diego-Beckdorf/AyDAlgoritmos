import sys

def is_sorted(A):
    aux = -1
    for num in A:
        if num < aux:
            return False
        aux = num
    return True

