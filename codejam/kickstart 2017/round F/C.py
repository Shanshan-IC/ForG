#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
这个题目是以Pokemon GO抓取宠物小精灵为背景，这儿有一款游戏叫Codejamon GO，去街道上抓取宠物小精灵。
你的城市有N个位置从1~N，你开始在位置1。这儿有M条双向的道路（1~M）。第i条道路连接两个不同的位置(Ui, Vi)，并且需要花Di分钟从一边到另一边。保证从位置1可以到其他任何位置。
在时间为0时，一个宠物小精灵会等概率出现在除了你当前位置（时间：0，位置：1）的其他任何位置。即每个位置出现宠物的概率为1/(N-1)。宠物一出现，你就会立刻抓住它，即抓取过程没有时间花费。每次只有一个宠物小精灵存在，只有抓住了存在的这个才会出现下一个。
给你城市布局，计算抓取P个宠物小精灵的期望时间，假设你在两个位置走的是最快的路线。

首先我们可以想到图的最短路算法，比如使用Dijkstra算法或Floyd-Warshall算法来计算两点的最短路径，在这个题目里即是时间最短的路径。
求出所有点之间的花费时间最少的路径的时间，后面会用到。
然后我们可以根据动态规划来计算期望时间，令dp[K, L]代表从位置L出发抓取K个精灵的期望时间，
然后我们可以得到状态转移方程：dp[K, L] = Σi!=L(dp[K-1, i] + dis[L, i]) / (N-1).
而dp[K, L] = 0 (K = 0)


'''

inf_num = float('inf')

def solve(cas, N, M, P, f, f_out):
    print('Case ', cas)
    ## dist 距离矩阵
    dist = [[inf_num for _ in xrange(N+1)] for _ in xrange(N+1)]
    for i in xrange(1, N+1):
        dist[i][i] = 0
    for i in xrange(M):
        tmp = [int(x) for x in f.readline().strip().split()]
        u, v, d = tmp
        dist[u][v] = d
        dist[v][u] = d
    # 计算最短距离矩阵
    for k in xrange(1, N+1):
        for i in xrange(1, N+1):
            for j in xrange(1, N+1):
                if dist[i][k] != inf_num and dist[k][j] != inf_num and dist[i][j] > dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    sum_all = 0
    for i in xrange(1, N+1):
        for j in xrange(1, N+1):
            sum_all += dist[i][j]
    sum_from_start = 0
    for i in xrange(2, N+1):
        sum_from_start += dist[1][i]
    exp, sum_exp = 0.0, 0.0
    for i in xrange(P):
        exp = (1.0/(N-1))*(sum_from_start+sum_exp-exp)
        sum_exp += (1.0/(N-1))*sum_all
    f_out.write('Case #%d: %f\n' % (cas+1, exp))


with open('C-large-practice.in', 'r') as f:
    with open('C-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            NMP = [int(x) for x in f.readline().strip().split()]
            N, M, P = NMP
            solve(cas, N, M, P, f, f_out)