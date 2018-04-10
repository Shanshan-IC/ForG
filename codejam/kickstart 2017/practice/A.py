def solve(str_l, n):
    set_l = [len(set(''.join([c for c in st if c.isalpha and c.isupper()]))) for st in str_l]
    maxs = max(set_l)
    str_max = [str_l[idx] for idx in xrange(n) if set_l[idx] == maxs]
    return min(str_max)

with open('A-large-practice.in', 'r') as f:
    with open('A-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            n = int(f.readline())
            str_l = []
            for i in xrange(n):
                str_l.append(f.readline())
            f_out.write('Case #%d: %s' % (cas+1, solve(str_l, n)))