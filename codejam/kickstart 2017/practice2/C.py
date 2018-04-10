# -*- coding: utf-8 -*-
'''
若是每一位都等于1，意味着x = a^0 + a^1+...a^k
'''

def helper(x, n):
    i = 0
    while n > 0:
        n -= x ** i
        i += 1
        print(n)
    return n == 0

with open('C-large-practice.in', 'r') as f:
    with open('C-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            n = int(f.readline())
            ans = n - 1
            print("case")
            for i in xrange(2, 64):
                tmp = int(n**(1.0/i))
                if tmp > 1:
                    ans = tmp if helper(tmp, n) else ans
            f_out.write('Case #%d: %d\n' % (cas+1, ans))