#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
dp[i][j] 表示到达i城时，已经参观了j个城的最少时间
情况1：dp[i-1][j]直接等车
情况2：dp[i-1][j-1] + 参观了i城的时间在等车
二者取最小值
最后取max{j | dp[N][j] < T}
'''

import math
def solve(N, Ts, Tf, S, F, D):
    dp = [[float("inf") for _ in xrange(N+1)] for _ in xrange(N+1)]
    dp[1][0] = 0
    for i in xrange(1, N):
        for j in xrange(N):
            # dp[i][j] + TS <= S[i] + F[i] * x
            # sightseen
            x = max(0, (dp[i][j] + Ts - S[i] + F[i] - 1) / F[i]) # x 表示到达等待的是第几趟车
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], S[i] + F[i] * x + D[i])
            # no sightseen
            x = max(0, (dp[i][j] - S[i] + F[i] - 1) / F[i])
            dp[i+1][j] = min(dp[i+1][j], S[i] + F[i] * x + D[i])
    res = -1
    for j in xrange(N):
        if dp[N][j] <= Tf:
            res = j
    res = str(res) if res >=0 else 'IMPOSSIBLE'
    return res

with open('A-large-practice.in', 'r') as f:
    with open('A-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            nm = [int(x) for x in f.readline().split(' ')]
            N, Ts, Tf = nm[0], nm[1], nm[2]
            condition = []
            for i in xrange(N-1):
                condition.append([int(x) for x in f.readline().split(' ')])
            condition = list(map(list, zip(*condition)))
            S, F, D = condition[0], condition[1], condition[2]
            S.insert(0, -1)
            F.insert(0, -1)
            D.insert(0, -1)
            print('case ', cas)
            f_out.write('Case #%d: %s\n' % (cas+1, solve(N, Ts, Tf, S, F, D)))


