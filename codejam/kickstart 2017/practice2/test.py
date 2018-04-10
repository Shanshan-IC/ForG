# from collections import *
# from itertools import *
# from heapq import *


def solve(N, L1, R1, A, B, C1, C2, M):
    x, y = L1, R1
    arrays = [(x, y)]
    for i in range(N - 1):
        x, y = (A * x + B * y + C1) % M, (A * y + B * x + C2) % M
        print(x, y)
        arrays.append((min(x, y), max(x, y)))
    res = float('inf')
    arrays.sort()
    print(arrays)
    res = [0] * N
    i0, l0, r0 = 0, arrays[0][0], arrays[0][1]
    for i, (l, r) in enumerate(arrays):
        if not i:
            continue
        if l > r0:
            res[i0] += r0 - l0 + 1
            i0, l0, r0 = i, l, r
        else:
            res[i0] += max(l - l0, 0)
            if r < r0:
                l0 = max(l0, r + 1)
            elif r > r0:
                i0 = i
                l0 = r0 + 1
                r0 = r
            else:
                l0 = r0 + 1
    res[i0] += r0 - l0 + 1
    # print arrays
    # print res
    print(cover(arrays), max(res))
    return cover(arrays) - max(res)


def cover(l):
    if not l:
        return 0
    res = 0
    l0, r0 = l[0]
    for l, r in l[1:]:
        if l > r0 + 1:
            res += r0 - l0 + 1
            l0, r0 = l, r
        else:
            r0 = max(r0, r)
    return res + r0 - l0 + 1


print(solve(1000, 1, 19, 15, 17, 14, 8, 20))

#
# def main():
#     T = int(fi.readline().strip())
#     for i in xrange(T):
#         N, L1, R1, A, B, C1, C2, M = map(int, fi.readline().strip().split())
#         res = solve(N, L1, R1, A, B, C1, C2, M)
#         out = "Case #%d: %s\n" % (i + 1, res)
#         print out
#         fo.write(out)


# print solve(*map(int, "2 630292702 923395676 0 0 518258315 208857809 924228249".split()))
# # print solve(*map(int, "4 257115776 621265131 0 0 51538675 456841891 962002799".split()))
# fi = open('D-small-practice.in', 'r')
# fo = open('D-large.out', 'w')
# main()
# fi.close()
# fo.close()
