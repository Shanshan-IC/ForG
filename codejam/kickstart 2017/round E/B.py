#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
不妨设梯形上底为 a，下底为 b，两腰为 c。有 a + 2c > b 且 a < b。遍历时可以分两种情况：

a ≠ b ≠ c
a = c 或 b = c（即有且仅有三边等）
情形 1 可以对 S 按 c, b, a 的顺序遍历。满足 a + 2c > b, a < b 且 a ≠ b ≠ c 时

ans += C(c.count, 2) * a.count * b.count
情形 2 对 c 遍历，然后对另一不等的边遍历，记为 a。满足 3c > a 且 a ≠ c 时

ans += C(c.count, 3) * a.count
'''
from collections import OrderedDict
from multiprocessing import Process

def solve(f_out, cas, N, sticks):
    print('case ', cas)
    sticks.sort()
    st_dict = OrderedDict()
    for s in sticks:
        if s not in st_dict:
            st_dict[s] = 1
        else:
            st_dict[s] += 1
    st_dict_l = list(st_dict.items())
    res, l = 0, len(st_dict_l)
    for a in xrange(l):
        for b in xrange(a+1, l):
            for c in xrange(l):
                if c != a and c != b  and st_dict_l[a][0]+2*st_dict_l[c][0] > st_dict_l[b][0]:
                    res += st_dict_l[a][1] * st_dict_l[b][1] * (st_dict_l[c][1]*(st_dict_l[c][1]-1)/2)
    for c in xrange(l):
        if st_dict_l[c][1] > 2:
            for a in xrange(l):
                if a != c and 3*st_dict_l[c][0] > st_dict_l[a][0]:
                    tmp = st_dict_l[c][1]
                    res += st_dict_l[a][1] * ((tmp*(tmp-1)*(tmp-2))/6)
    f_out.write('Case #%d: %s\n' % (cas + 1, res))

import time
start_time = time.clock()

with open('B-large-practice.in', 'r') as f:
    with open('B-large.out', 'w+') as f_out:
        t = int(f.readline())
        ps = list()
        for cas in xrange(t):
            N = int(f.readline().strip())
            sticks = [int(x) for x in f.readline().strip().split()]
            p = Process(target=solve, args=(f_out, cas, N, sticks))
            ps.append(p)
            p.start()
        for proc in ps:
            proc.join()


print(time.clock() - start_time)