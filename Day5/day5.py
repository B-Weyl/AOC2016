import sys
import hashlib
infile = sys.argv[1] if len(sys.argv) > 1 else 'day5.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day5test.txt'

doorID = 'ffykfhsq'
# doorID = "abc"
pw = ""
pw2 = [' '] * 8

legal = list('01234567')
for x in range(30_000_000):
    result = hashlib.md5((doorID + str(x)).encode())
    ans = result.hexdigest()
    if ans[:5] == '00000':
        if len(pw) < 8:
            pw += ans[5]
        if ans[5] in legal and pw2[int(ans[5])] == ' ':
            pw2[int(ans[5])] = ans[6]
        else:
            continue
    if ' ' not in pw2:
        break
print(pw)
print(''.join(pw2))
