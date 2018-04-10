# -*- coding: utf-8 -*-

'''
http://blog.csdn.net/kyoma/article/details/60591058
res = [(1+n)*n/2] * [(nm+n+m+1) - (n+m+1)*(2n+1)/3 + n(n+1)/2]
难点涉及了除法的模运算
对于 Python 来说，其弱类型就导致了当声明 1e9+7 的时候，默认会作为浮点数，
若不注意强转数据类型，float 对最终的大整数取模将产生致命的错误。
由于 Python 的整型可以自动支持大整数，也不用专门去化简之类的。
'''

mod = 1000000007
INV2 = (mod + 1) / 2
INV3 = (mod + 1) / 3

def solve(n, m):
    if m < n:
        n, m = m, n
    c1 = n * (n+1) / 2 % mod
    c2 = (((c1* (2*n+1)) % mod) * INV3) %mod
    c3 = c1 * c1 % mod
    ans = n*m % mod * c1 % mod
    ans = (ans - (n+m)*c2) % mod
    ans = (ans + c3) % mod
    return (ans+mod)%mod

def solve_2(n, m):
    k = min(n, m)
    c1 = (1+k)*k/2
    res = c1 * ((n*m+n+m+1) - (n+m+1)*(2*n+1)/3 + c1) % mod
    return res

with open('A-large-practice.in', 'r') as f:
    with open('A-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            nm = [int(x) for x in f.readline().split(' ')]
            n, m= nm[0], nm[1]
            f_out.write('Case #%d: %d\n' % (cas+1, solve(n, m)))
