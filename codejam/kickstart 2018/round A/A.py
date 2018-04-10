

def solve(n):
    res, i = 0, 0
    ss = str(n)
    number = [int(s) for s in ss]
    while (i < len(number)-1):
        if number[i]&1:
            tmp1 = (number[i]+1)*10 if number[i]< 9 else 1000000
            tmp2 = (number[i]-1)*10 + 8
            cur = number[i] * 10 + number[i + 1]
            now_n = 0 if i == 0 else (int(ss[:i]) * (10 ** (len(number) - i)))
            now_n1 =  now_n + tmp1 * (10**(len(number)-i-2))
            now_n2 = now_n + tmp2 * (10**(len(number)-i-2))
            for kkk in xrange(i+2, len(number)):
                now_n2 += 8*(10**(len(number)-kkk-1))
            return min(n - now_n2, now_n1-n)
        else:
            i += 1
    return 0 if (number[len(number)-1]&1 == 0) else 1

with open('A-large-practice.in', 'r') as f:
    with open('A-large.out', 'w') as f_out:
        t=int(f.readline())
        for i in xrange(t):
            n = int(f.readline())
            f_out.write("Case #%d: %ld\n" % (i+1, solve(n)))
