
import math
def solve(ss, l, r):
    if r < l:
        return 0
    sz = len(ss)
    cur, res = 0, 0
    for c in ss:
        if c == 'B':
            cur += 1
    res += (r-l)/sz * cur
    j = (r-l)%sz + l
    for k in xrange(l, j+1):
        if ss[k%sz] == 'B':
            res += 1
    return res

with open('A-large-practice.in', 'r') as f:
    with open('A-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            ss = f.readline().rstrip('\n')
            print(ss)
            ab = [long(x) for x in f.readline().split(' ')]
            a, b = ab[0], ab[1]
            print(a, b)
            f_out.write('Case #%d: %ld\n' % (cas+1, solve(ss, a-1, b-1)))