import sys

with open('A-large-practice.in', 'r') as f:
    with open('A-large.out', 'w+') as f_out:
        tc = int(f.readline())
        for i in xrange(tc):
            f_out.write("Case #%d:\n" % (i+1))
            r, c = map(int, f.readline().split())
            ll = []
            for _ in xrange(r):
                ll.append(f.readline().strip())
            z = 0
            while ll[z] == '?' * c:
                z += 1
            last = ll[z]
            for i in xrange(r):
                if ll[i] == '?' * c:
                    ls = last
                else:
                    ls = ll[i]
                last = ls
                y = 0
                while ls[y] == '?': y += 1
                lc = ls[y]
                tt = []
                for cc in ls:
                    if cc == '?':
                        f_out.write(lc)
                    else:
                        f_out.write(cc)
                        lc = cc
                f_out.write('\n')