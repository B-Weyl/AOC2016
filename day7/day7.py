from itertools import pairwise
from more_itertools import windowed
ips = [x.strip() for x in open('day7.txt').readlines()]


def containsPalin(word):
    #if word already meets criteria - return True
    if len(word) < 4:
        return False
    for x in range(len(word) - 3):
        if word[x:x+4] == word[x:x+4][::-1] and word[x] != word[x +1]:
            return True
    return False

def containsSSL(ip):
    ip = ip.replace('[', ' ').replace(']', ' ')
    i = ip.split(' ')
    even = []
    odd = []
    for x in range(len(i)):
        if x % 2 == 0:
            even.append(i[x])
        else:
            odd.append(i[x])
    for e in even:
        checks = getWindows(e)
        for c in checks:
            if c[0] == c[2] and c[0] != c[1]:
                nc = c[1] + c[0] + c[1]
                for o in odd:
                    if nc in o:
                        return True
                        break
    return False 
                
                    
    

def getWindows(ip):
    # make the e value = to what the odd value should be and check
    # if it is in the corresponding list
    pairs = windowed(ip, n=3, step=1)
    return [''.join(p) for p in pairs]
    
#Part 1
part1 = 0
for ip in ips:
    bad = False
    found = False
    new_ip = ip.replace('[', ' ').replace(']', ' ')
    for x, y in enumerate(new_ip.split(' ')):
        if x % 2 == 1 and containsPalin(y):
            bad = True
        else:
            if containsPalin(y):
                # print(x, y)
                found = True

    if found and not bad:
        part1 += 1

part2 = 0
for ip in ips:
    if containsSSL(ip):
        part2 += 1
                    
print(part1, part2)
        

    
    

    
    
    
    

        
        
        
