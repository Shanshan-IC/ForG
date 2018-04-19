#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
解法1：四平方和定理
https://zh.wikipedia.org/wiki/%E5%9B%9B%E5%B9%B3%E6%96%B9%E5%92%8C%E5%AE%9A%E7%90%86
说明每个正整数均可表示为4个整数的平方和。它是费马多边形数定理和华林问题的特例。
注意有些整数不可表示为3个整数的平方和，例如7。
http://www.cnblogs.com/grandyang/p/4800552.html
'''
import math
def solve(n):
    while n % 4 ==0:
        n /= 4
    if n % 8 == 7:
        return 4
    a = 0
    while a * a <= n:
        b = int(math.sqrt(n - a*a))
        if a * a + b *b ==n:
            return int(a>0) + int(b>0)
        a += 1
    return 3


with open('D-large-practice.in', 'r') as f:
    with open('D-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            N = int(f.readline())
            f_out.write('Case #%d: %s\n' % (cas+1, solve(N)))