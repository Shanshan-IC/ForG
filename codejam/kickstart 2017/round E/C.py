#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
小数据由于只在一条线上，直接除以6就可以了。


'''
with open('C-small-practice.in', 'r') as f:
    with open('C-small.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            balls = []
            for _ in xrange(3):
                balls.append([int(x) for x in f.readline().strip().split()])
            balls.sort()
            print(balls)
            f_out.write('Case #%d: %f\n' %(cas+1, (balls[2][0]-balls[0][0])/6.0))