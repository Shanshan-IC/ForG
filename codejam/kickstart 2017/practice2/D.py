
def cover(arr):
    if not arr:
        return 0
    res = 0
    l0 , r0 = arr[0]
    for l, r in arr[1:]:
        if l > r0 + 1:
            res += r0-l0+1
            l0, r0 = l, r
        else:
            r0 = max(r0, r)
    return res + r0 - l0 + 1

def solve(n, l1, r1, a, b, c1, c2, m):
    print((n, l1, r1, a, b, c1, c2, m))
    arr = [(l1, r1)]
    for i in xrange(n-1):
        l1 = (a*l1+ b*r1 + c1) % m
        r1 = (a*r1+ b*l1 + c2) % m
        arr.append((min(l1, r1), max(l1, r1)))
    arr.sort()
    print(arr)
    res = [0] * n
    i0, l0, r0 = 0, arr[0][0], arr[0][1]
    for i, (l, r) in enumerate(arr):
        if not i:
            continue
        if l > r0:
            res[i0] += r0 - l0 + 1
            i0, l0, r0 = i, l, r
        else:
            res[i0] += max(l-l0, 0)
            if r < r0:
                l0 = max(l0, r + 1)
            elif r > r0:
                i0, l0, r0 = i, r0+1, r
            else:
                l0 = r0 + 1
    res[i0] += r0-l0+1
    print(cover(arr), max(res))
    return cover(arr) - max(res)

print(solve(1000, 1, 19, 15, 17, 14, 8, 20))
#
# with open('D-small-practice.in', 'r') as f:
#     with open('D-small.out', 'w+') as f_out:
#         t = int(f.readline())
#         for cas in xrange(t):
#             N, L1, R1, A, B, C1, C2, M = map(int, f.readline().strip().split())
#             f_out.write('Case #%d: %d\n' % (cas+1, solve(N, L1, R1, A, B, C1, C2, M)))