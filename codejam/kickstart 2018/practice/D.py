# -*- coding: utf-8 -*-

def sub_lists(my_list):
    subs = []
    for i in range(len(my_list)):
        n = i + 1
        while n <= len(my_list):
            sub = my_list[i:n]
            subs.append(sum(sub))
            n += 1
    return sorted(subs)


'''
怎么快速地求出区间[l, r]区间的和
'''

with open('D-large-practice.in', 'r') as f:
    with open('D-large.out', 'w') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            nq = [int(i) for i in f.readline().strip().split(' ')]
            N, Q = nq[0], nq[1]
            arr = [int(i) for i in f.readline().strip().split(' ')]
            f_out.write("Case #%d:\n" % (cas + 1))
            # a表示左侧的累加和
            arr.insert(0, 0)
            for i in xrange(1, N + 1):
                arr[i] += arr[i - 1]
            s = [0 for _ in xrange(N + 1)]
            for i in xrange(1, N + 1):
                s[i] = s[i - 1] + arr[i]
            for i in xrange(Q):



