# -*- coding: utf-8 -*-


'''
http://blog.csdn.net/angelniu1024/article/details/71513212
https://www.quora.com/How-do-I-solve-the-Center-of-Google-Kickstart-2017-B-Round-2
http://haogram.hol.es/index.php/archives/32/
我们可以发现在曼哈顿距离中，X轴方向的距离和Y轴方向的距离无关，且相互没有影响，故可以单独计算。
即sigma(|X-Xi|+|Y-Yi|) = sigma(|X-Xi|) + sigma(|Y-Yi|)，
据此我们可以先按照x排序，计算以每个x值为中心时X轴方向上的距离和，然后按照y排序，
计算以每个y值为中心时Y轴方向上的距离和。

使用的是曼哈顿距离的属性：
max(|X-x|, |Y-y|) = |X-x| + |Y-y|
三分法搜索
然后分别对X，Y进行三分，X方向距离和的最小值加上Y方向距离和的最小值，即为最终解。
三分法介绍：http://www.voidcn.com/article/p-grlcitji-s.html
1.先将区间三分,每个区间的长度为1/3(right-left)
mid1=left+(right-left)/3;
mid2=right-(right-left)/3;
2.比较mid1和mid2谁更靠近极值，如果mid1更靠近极值，右区间改为mid2,否则左区间改为mid1(后面的代码都是   以求最大值为例）
if(calc(mid1)<calc(mid2))
left=mid1;
else
right=mid2;

双层的三分法嵌套，固定X后继续三分法寻找Y
'''

def calc_score(arr, x, y):
    res = 0.0
    for a in arr:
        res += max(abs(a[0]-x), abs(a[1]-y)) * a[2]
    return res

def calc(arr, m):
    l, r = -10000.0, 10000.0
    T = 100
    while T:
        m1 = (l * 2 + r) / 3
        m2 = (l + 2 * r) / 3
        f1 = calc_score(arr, m, m1)
        f2 = calc_score(arr, m, m2)
        if f1 < f2:
            r = m2
        else:
            l = m1
        T -= 1
    return calc_score(arr, m, l)

def solve(arr):
    l, r = -10000.0, 10000.0
    T = 100
    while T:
        m1 = (l*2+r) / 3
        m2 = (l+2*r) / 3
        f1 = calc(arr, m1)
        f2 = calc(arr, m2)
        if f1 < f2:
            r = m2
        else:
            l = m1
        T -= 1
    return calc(arr, l)

with open('B-large-practice.in', 'r') as f:
    with open('B-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            n = int(f.readline())
            arr = []
            print(cas)
            for i in xrange(n):
                arr.append([float(i) for i in f.readline().split(' ')])
            f_out.write('Case #%d: %f\n' % (cas+1, solve(arr)))