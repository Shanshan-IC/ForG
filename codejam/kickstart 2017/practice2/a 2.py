def proc(x, n):
    i=0
    while n>0:
        n -= x**i
        i+=1
    return n==0
for _ in range(1,input()+1):
    n=input()
    ans = n-1
    for i in range(2, 64):
        if int(n**(1.0/i))>1:
            ans = int(n**(1.0/i)) if proc(int(n**(1.0/i)), n) else ans
        else:break
    print "Case #"+str(_)+":", ans
