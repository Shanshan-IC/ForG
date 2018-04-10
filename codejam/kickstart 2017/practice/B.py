with open('B-small-practice.in', 'r') as f:
    with open('B-small.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            nm = [int(x) for x in f.readline().split(' ')]
            n, m= nm[0], nm[1]
            f_out.write('Case #%d: %f\n' % (cas+1, (n-m)*1.0 / (n+m)))
