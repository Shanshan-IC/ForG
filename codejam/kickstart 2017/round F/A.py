#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(N, arr):
    mins, maxs = 1, N
    flag = True
    while len(arr) > 1 and (len(arr)-1)/2 >= 0:
        p = (len(arr) - 1) /2
        pivot = arr[p]
        if pivot == mins:
            arr.remove(pivot)
            mins += 1
        elif pivot == maxs:
            arr.remove(pivot)
            maxs -= 1
        else:
            flag = False
            break
    del arr
    res = 'YES' if flag else 'NO'
    return res

with open('A-large-practice.in', 'r') as f:
    with open('A-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            N = int(f.readline())
            arr = [int(x) for x in f.readline().strip().split()]
            f_out.write('Case #%d: %s\n' % (cas+1, solve(N, arr)))