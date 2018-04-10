
with open('A-large-practice.in', 'r') as f:
    with open('A-large.out', 'w') as f_out:
        t=int(f.readline())
        for cas in xrange(t):
            n = int(f.readline())
            arr = [int(i) for i in f.readline().strip().split(' ')]
            p = int(f.readline())
            record = [0 for i in xrange(5001)]
            for i in xrange(n):
                l = min(arr[2*i], arr[2*i+1])
                r = max(arr[2*i], arr[2*i+1])
                for j in xrange(l, r+1):
                    record[j] += 1
            res = [str(record[int(f.readline())]) for _ in xrange(p)]
            f_out.write("Case #%d: %s\n" % (cas+1, ' '.join(res)))
            f.readline()
