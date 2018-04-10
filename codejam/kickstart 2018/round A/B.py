# -*- coding: utf-8 -*-

# 计算有放回的等概率球的返回概率
# def calc(n, k):
#     res = 0.0
#     pa = 1.0 /n
#     pb = 1 - 1.0 / n
#     for i in xrange(k):
#         res += (pb ** i)*pa
#     return res

def calc(n, k):
    res = 0.0
    pb = 1 - 1.0 / n
    return 1-pb**k

def solve(arr, n, k):
    arr.sort(reverse =True)
    remove_prob, res = 0.0, 0.0
    for i in xrange(n):
        cur = calc(n-i, k+1)
        res += arr[i] * (1 - remove_prob) * cur
        remove_prob += (1 - remove_prob) * cur
    return res

print(solve([16, 11, 7, 4, 1], 5, 3-1))
with open('B-small-practice.in', 'r') as f:
    with open('B-small.out', 'w') as f_out:
        t=int(f.readline())
        for i in xrange(t):
            nk = [int(x) for x in f.readline().split(' ')]
            arr = [int(x) for x in f.readline().split(' ')]
            f_out.write("Case #%d: %f\n" % (i+1, solve(arr, nk[0], nk[1])))
