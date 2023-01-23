import sys
infile = sys.argv[1] if len(sys.argv) > 1 else 'day2.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day2test.txt'

digits = [x.strip() for x in open(infile).readlines()]
starting = [0, 0]
starting2 = [0, 0]
checkstring = [0, 0]
cur = [0, 0]

# part 1
KEYPAD = {
    (-1, 1): '1',
    (0, 1): '2',
    (1, 1): '3',
    (-1, 0): '4',
    (0, 0): '5',
    (1, 0): '6',
    (-1, -1): '7',
    (0, -1): '8',
    (1, -1): '9'
}
# part 2
KEYPAD2 = {
    (2, 2): '1',
    (1, 1): '2',
    (2, 1): '3',
    (3, 1): '4',
    (0, 0): '5',
    (1, 0): '6',
    (2, 0): '7',
    (3, 0): '8',
    (4, 0): '9',
    (1, -1): 'A',
    (2, -1): 'B',
    (3, -1): 'C',
    (2, -2): 'D'
}

# 1982
NUM = []
NUM2 = []
for number in digits:
    for n in number:
        match n:
            case 'U':
                starting[1] += 1
            case 'D':
                starting[1] -= 1
            case 'L':
                starting[0] -= 1
            case 'R':
                starting[0] += 1
        if starting[0] > 1:
            starting[0] = 1
        if starting[0] < -1:
            starting[0] = -1
        if starting[1] > 1:
            starting[1] = 1
        if starting[1] < -1:
            starting[1] = -1
    NUM.append(KEYPAD[starting[0], starting[1]])
print(''.join(NUM))




for number in digits:
    for n in number:
        # cur = starting2
        match n:
            case 'U':
                if (starting2[0], starting2[1] + 1) in KEYPAD2.keys():
                    starting2[1] += 1
            case 'D':
                if (starting2[0], starting2[1] - 1) in KEYPAD2.keys():
                    starting2[1] -= 1
            case 'L':
                if (starting2[0] - 1, starting2[1]) in KEYPAD2.keys():
                    starting2[0] -= 1
            case 'R':
                if (starting2[0] + 1, starting2[1]) in KEYPAD2.keys():
                    starting2[0] += 1
    NUM2.append(KEYPAD2[starting2[0], starting2[1]])
print(''.join(NUM2))


            


