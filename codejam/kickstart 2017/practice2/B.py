

def solve(matrix, dp, r, c):
    ans = 0
    for i in xrange(r):
        for j in xrange(c):
            if matrix[i][j] == 0:
                # 当周围都是野兽则不可能，只包含自己方格1，
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans += dp[i][j]
    return ans


with open('B-large-practice.in', 'r') as f:
    with open('B-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            rck = [int (x) for x in f.readline().split(' ')]
            r, c, k = rck[0], rck[1], rck[2]
            matrix = [[0 for i in xrange(c)] for _ in xrange(r)]
            for i in xrange(k):
                ab = [int (x) for x in f.readline().split(' ')]
                matrix[ab[0]][ab[1]] = 1
            dp = [[0 for i in xrange(c+1)] for _ in xrange(r+1)]
            f_out.write('Case #%d: %d\n' % (cas+1, solve(matrix, dp, r, c)))