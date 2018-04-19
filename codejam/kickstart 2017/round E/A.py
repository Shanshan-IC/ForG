#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
dp[i][j][k]，0 ≤ j < k ≤ i ≤ len，表示已经输入了前 i 个字母，剪贴板中的字符为 substr[j,k) 时，所需的最少的操作数。
用 dp[i][0][0] 表示 min{dp[i][j][k] | 0 ≤ j < k ≤ i}。或者另开一个一维数组来维护也行。
初值为 dp[0][0][0] = 0，其他为正无穷。
'''

def solve(s):
    l = len(s)
    dp = [[[float("inf") for _ in xrange(l+1)] for _ in xrange(l+1)] for _ in xrange(l+1)]
    dp[0][0][0] = 0
    for i in xrange(l):
        dp[i+1][0][0] = min(dp[i+1][0][0], dp[i][0][0]+1) # 直接输入一个字母
        for j in xrange(i):
            for k in xrange(j+1, i+1):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k]+1) # 直接输入一个字母
                # 粘贴板上的字符串是str[i:]为起始的一部分
                if s[i:].startswith(s[j:k]):
                    dp[i+k-j][j][k] = min(dp[i+k-j][j][k], dp[i][j][k]+1) # 输入粘贴板
                    dp[i+k-j][j][k] = min(dp[i+k-j][j][k], dp[i][0][0]+2) # 先复制再黏贴
                    dp[i+k-j][0][0] = min(dp[i+k-j][0][0], dp[i][j][k]+1)
                    dp[i+k-j][0][0] = min(dp[i+k-j][0][0], dp[i][0][0]+2)
    return dp[l][0][0]

with open('A-large-practice.in', 'r') as f:
    with open('A-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            inp = f.readline().strip()
            f_out.write('Case #%d: %s\n' % (cas+1, solve(inp)))