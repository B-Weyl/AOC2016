import sys
from itertools import pairwise
infile = sys.argv[1] if len(sys.argv) > 1 else 'day3.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day3test.txt'

part1 = 0
triangles = open(infile).readlines()
for triangle in triangles:
    a, b, c = [int(x) for x in triangle.split()]
    
    if a + b > c and a + c > b and c + b > a:
        part1 += 1
print(part1)

# part 2 - break into three arrays, add totals from each
triangles2 = open(infile).readlines()
A, B, C = [], [], []
part2 = 0
for triangle2 in triangles2:
    a, b, c = [int(x) for x in triangle2.split()]
    A.append(a)
    B.append(b)
    C.append(c)

for x in range(0,len(A),3):
    if A[x] + A[x+1] > A[x+2] and A[x] + A[x+2] > A[x+1] and A[x+1] + A[x+2] > A[x]:
        part2 += 1

for x in range(0,len(B),3):
    if B[x] + B[x+1] > B[x+2] and B[x] + B[x+2] > B[x+1] and B[x+1] + B[x+2] > B[x]:
        part2 += 1

for x in range(0,len(C),3):
    if C[x] + C[x+1] > C[x+2] and C[x] + C[x+2] > C[x+1] and C[x+1] + C[x+2] > C[x]:
        part2 += 1
print(part2)


