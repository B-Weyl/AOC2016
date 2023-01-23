import sys
infile = sys.argv[1] if len(sys.argv) > 1 else 'day9.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day9test.txt'

data = open(infile).read()
print(data)


ans = []
value = []
for x in range(len(data)):
    if data[x] != ')':
        value.append(data[x])






