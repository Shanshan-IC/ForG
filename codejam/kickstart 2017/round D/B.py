#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
首先矩阵有两个性质：
A·B 的子矩阵等价于 A 的一个子向量 和 B 的一个子向量 的积
Sum(A·B) = Sum(A)·Sum(B)
所以题目可以简化为，先求 A 和 B 的全部子向量的区间和，记为 SA 和 SB，再求第 K 大的 SA[i] * SB[j]。


'''


with open('B-small-practice.in', 'r') as f:
    with open('B-small.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            nm = [int(x) for x in f.readline().split(' ')]
            N, K, A1, B1, C, D, E1, E2, F = nm
            x, y, r, s = [A1], [B1], [-1, 0], [-1, 0]
            for i in xrange(1, N):
                x.append(C * x[i-1] + D * y[i-1] + E1) % F
                y.append(D * x[i - 1] + C * y[i - 1] + E2) % F
                r.append(C * r[i-1] + D * s[i-1] + E1) % 2
                s.append(D * r[i - 1] + C * s[i - 1] + E2) % 2
            A, B, pA, pB = [], [], [], []
            for i in xrange(N):
                A.append((-1)**r[i] * x[i])
                B.append((-1)**s[i] * y[i])
