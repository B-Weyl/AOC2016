import sys
from collections import Counter
import string
infile = sys.argv[1] if len(sys.argv) > 1 else 'day4.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day4test.txt'

part1 = 0
p1 = []
rooms = open(infile).readlines()
for r in rooms:
    # name
    words = r.split('-')
    # sectorID, checksum
    value, check = words[-1].split('[')
    check = check.strip()[:-1]
    letters = ''.join(words[:-1])
    L = Counter(letters)
    sortedL = dict(sorted(L.items(), key = lambda x: (-x[1],x[0])))
    S = ''.join(x for x in sortedL.keys())
    if S[:5] == check:
        part1 += int(value)
print(part1)

# part 2 
C = list(string.ascii_lowercase)
C.insert(0, C.pop())
print(C)
cipher = list('zabcdefghijklmnopqrstuvwxy')

A = []
for r in rooms:
    words = r.split('-')
    letters2 = list(' '.join(words[:-1]))
    value, check = words[-1].split('[')
    value = int(value)
    moves = value % 26
    ans = []
    # move each letter by (value number of spaces % 26)
    for l2 in letters2:
        if l2 != ' ':
            v = 26 - (122 - ord(l2))
            ans.append(cipher[(v + moves) % 26])
    # print(''.join(ans))

            

    

    
