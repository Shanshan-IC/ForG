# -*- coding: utf-8 -*-

'''
首先，第k个数的长度是2^k+1，且所有的2^i位置必是0
B[k]以下性质
1. 处在2次幂位置的数必定为0
2. 如果k是偶数，B[k]=B[k/2]
3. 如果k是奇数，k=2i+1，B[k]=i%2
'''

def solve(n):
    if (n & (n-1)) == 0:
        return 0
    while n > 0 and (n & 1) == 0:
        n >>= 1
    n >>= 1
    return n & 1

with open('B-small-practice.in', 'r') as f:
    with open('B-small.out', 'w') as f_out:
        t=int(f.readline())
        for i in xrange(t):
            n = int(f.readline())
            f_out.write("Case #%d: %d\n" % (i+1, solve(n)))

