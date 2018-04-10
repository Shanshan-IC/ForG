mod = 1000000007
import math
def solve(arr, n):
    res = 0
    for i in xrange(1, n):
        # res += arr[i]*(math.pow(2, i)-1)
        res += arr[i]*(2**i-1)
    for i in xrange(n-1):
        # res -= arr[i]*(math.pow(2, n-i-1)-1)
        res -= arr[i]*(2**(n-i-1)-1)
    return res % mod

with open('A-large-practice.in', 'r') as f:
    with open('A-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            n = int(f.readline())
            arr = [int(i) for i in f.readline().split(' ')]
            f_out.write('Case #%d: %d\n' % (cas+1, solve(arr, n)))