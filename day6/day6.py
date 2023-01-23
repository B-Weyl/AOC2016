from collections import Counter


message = open('day6.txt').readlines()
# print(message)
ans1 = ""
ans2 = ""


for x in range(len(message[0]) - 1):
    counts = Counter(a[x] for a in message)
    ans1 += ''.join(counts.most_common()[0][0])
    ans2 += counts.most_common()[-1][0]
    
    
print(ans1)
print(ans2)
    