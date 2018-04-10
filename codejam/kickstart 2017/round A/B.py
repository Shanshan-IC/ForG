
def get_new(s):
    new_s = ''
    for i in s:
        if i == '*':
            new_s += '0000'
        else:
            new_s += i
    return new_s

def solve(pattern, s):
    pattern = get_new(pattern)
    s = get_new(s)
    m, n = len(pattern), len(s)
    dp = [[0 for i in xrange(n+1)] for _ in xrange(m+1)]
    dp[0][0] = 1
    for i in xrange(m):
        for j in xrange(n):
            if dp[i][j]:
                dp[i][j+1] |= s[j] == '0'
                dp[i+1][j] |= pattern[i] == '0'
                dp[i+1][j+1] |= s[j] == '0' or pattern[i] == '0' or s[j] == pattern[i]
    res = 'True' if dp[m][n] else 'False'
    return res

with open('B-large-practice.in', 'r') as f:
    with open('B-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            pattern = f.readline()
            s = f.readline()
            print(cas)
            f_out.write('Case #%d: %s\n' % (cas+1, solve(pattern, s)))