#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
有N个卡片，正反各有一个正整数。玩家初始分数0分，每次选两张卡片，分别将其中一张的正面和另一张的反面异或，并将结果加到总分上。结束后将一张卡片丢弃，另一张放回，由此重复一直到只有一张卡片。求最终最小的分数。
查看题解，题解使用图论的观点来看，由于每次操作都有一张卡片被消去，我们假设卡片i被j消去，可以看做从i到j存在一条边。
于是恍然大悟，这条就是个最小生成树啊，套个模板就出来了。
'''
def dsu(x, part):
    if x == part[x]:
        return x
    part[x] = dsu(part[x], part)
    return part[x]

def solve(n, R, B):
    # 有向图,对获得分数排列
    edges = []
    for i in xrange(n):
        for j in xrange(i + 1, n):
            edges.append((min(R[i] ^ B[j], R[j] ^ B[i]), i, j))
    edges.sort()
    part = [i for i in xrange(n)]
    res = 0
    for i in xrange(len(edges)): # 从小到达累加边权重
        w, u, v = edges[i]
        if dsu(u, part) != dsu(v, part): # 如果从u点到v点还能畅通（点都未被使用）
            part[dsu(u, part)] = dsu(v, part) # u点被扔掉，v点放回
            res += w
    return res


with open('B-small-practice.in', 'r') as f:
    with open('B-small.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            N = int(f.readline())
            R = [int(x) for x in f.readline().strip().split()]
            B = [int(x) for x in f.readline().strip().split()]
            f_out.write('Case #%d: %d\n' % (cas + 1, solve(N, R, B)))
