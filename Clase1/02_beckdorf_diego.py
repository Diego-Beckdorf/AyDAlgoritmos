import sys


while True:
    line = sys.stdin.readline().split()
    bins = [0, 1, 2]
    if line is None:
        break
    bottles = [int(b) for b in line.split()]
    B_bottles = bottles[:2]
    G_bottles = bottles[3:5]
    C_bottles = bottles[6:8]
    bottles_moved = -1
        
    
    