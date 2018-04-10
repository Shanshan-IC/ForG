# -*- coding: utf-8 -*-


'''
http://blog.csdn.net/fcxxzux/article/details/52346364
只能是()()()()这样的形式返回最多

'''

with open('C-large-practice.in', 'r') as f:
    with open('C-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            nm = [int(x) for x in f.readline().split(' ')]
            n, m= nm[0], nm[1]
            param = min(n, m)
            f_out.write('Case #%d: %d\n' % (cas+1, param *(param+1) / 2))