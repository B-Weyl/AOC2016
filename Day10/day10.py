import sys
infile = sys.argv[1] if len(sys.argv) > 1 else 'day10.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day10test.txt'


bots = {}
O  = []
I = []
instructions = open(infile).readlines()
for i in instructions:
    words = i.split()
    if words[0] == 'bot':
        source, low, high = words[1], words[6], words[11]
        if words[5] == 'bot': 
            bots[words[6]] = min(bots[source])
        if words[5] == 'output': 
            O.append(min(bots[source]))
        if words[5] == 'input': 
            I.append(min(bots[source]))
        
        if words[10] == 'bot':
            bots[words[11]] = max(bots[source])
        



            
        
    


        




    