

def sort_flight(s, l):
    before = {s[2*i]: i for i in xrange(l)}
    after = {s[2*i+1]: i for i in xrange(l)}
    res = [0]
    while (s[2*res[-1]+1] in before):
        res.append(before[s[2*res[-1]+1]])
    if len(res) == l:
        return res
    else:
        while (s[2*res[0]] in after):
            res.insert(0, after[s[2*res[0]]])
    return res


with open('C-large-practice.in', 'r') as f:
    with open('C-large.out', 'w+') as f_out:
        t=int(f.readline())
        for cas in xrange(t):
            n = int(f.readline())
            flights = []
            for i in xrange(2*n):
                flights.append(f.readline().rstrip('\n'))
            res = sort_flight(flights, n)
            res_str = ' '.join(['%s-%s'% (flights[2*r], flights[2*r+1]) for r in res])
            f_out.write("Case #%d: %s\n" % (cas+1, res_str))
