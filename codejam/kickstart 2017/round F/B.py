#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(arr, E, N):
    arr.sort()
    l, r, coins, energy = 0, N-1, 0, E
    while (l <= r):
        if energy > arr[l]:
            coins += 1
            energy -= arr[l]
            l += 1
        elif coins > 0 and arr[r] > arr[l]:
            coins -= 1
            energy += arr[r]
            r -= 1
        else:
            break
    del arr
    return coins

with open('B-large-practice.in', 'r') as f:
    with open('B-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            EN = [int(x) for x in f.readline().strip().split()]
            E, N = EN
            arr = [int(x) for x in f.readline().strip().split()]
            f_out.write('Case #%d: %d\n' % (cas+1, solve(arr, E, N)))
