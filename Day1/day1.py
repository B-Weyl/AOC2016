import sys
infile = sys.argv[1] if len(sys.argv) > 1 else 'day1.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day1test.txt'
L = [0, 0]
deg = 0
visited = set()


steps = open(infile).read()
steps = list(steps.split(', '))
for step in steps:
    amt = int(step[1:].strip())
    match step[0]:
        case 'R':
            deg += 90
            deg = deg % 360
        case 'L':
            deg -= 90
            deg = deg % 360
    if deg == 90:
        for a in range(amt):
            L[0] += 1
            if (L[0], L[1]) not in visited:
                visited.add((L[0], L[1]))
            else:
                print(abs(L[0]) + abs(L[1]))
                break
    elif deg == 180:
        for a in range(amt):
            L[1] -= 1
            if (L[0], L[1]) not in visited:
                visited.add((L[0], L[1]))
            else:
                print(abs(L[0]) + abs(L[1]))
                break
    elif deg == 270:
        for a in range(amt):
            L[0] -= 1
            if (L[0], L[1]) not in visited:
                visited.add((L[0], L[1]))
            else:
                print(abs(L[0]) + abs(L[1]))
                break
    else:
        for a in range(amt):
            L[1] += 1
            if (L[0], L[1]) not in visited:
                visited.add((L[0], L[1]))
            else:
                print(abs(L[0]) + abs(L[1]))
                break

# print(abs(L[0]) + abs(L[1]))


    
    




