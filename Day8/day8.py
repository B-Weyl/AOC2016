import sys
import numpy as np
infile = sys.argv[1] if len(sys.argv) > 1 else 'day8.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day8test.txt'
width = 7
height = 3

# starts with all off
GRID = [list(['0']) * width] * height
G = np.zeros((6, 50))


# rect (3, 2) -> [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]


I = open(infile).readlines()
for i in I:
    words = i.split()
    if words[0] == 'rect':
        A, B = [int(x) for x in words[1].split('x')]
        for b in range(B):
            for a in range(A):
                G[b][a] = 1
    elif words[1] == 'column':
        xcoord, amt = words[2], int(words[-1])
        x = int(xcoord.split('=')[1])
        G[:, x] = np.roll(G[:, x], amt)
    elif words[1] == 'row':
        ycoord, amt = words[2], int(words[-1])
        y = int(ycoord.split('=')[1])
        G[y, :] = np.roll(G[y, :], amt)



L = np.ndarray.tolist(G)
for l in L:
    print(l)

# print(L)
# print(G.sum())
# print(list(G))

    
