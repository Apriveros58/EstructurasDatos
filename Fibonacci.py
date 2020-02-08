def fibo(n):
    act = 0
    sig = 1
    for t in range(n):
        res = act + sig
        act = sig
        sig = res
    return sig
print(fibo(10))

def fibo_rec(n, t, ac, si):
    if t < n:
        re = ac
        ac = ac + si
        si = re
        t=t+1
        fibo_rec(n, t, ac, si)
    else:
        print(ac+si)
t=1
ac=1
si=0
print(fibo_rec(10, t, ac, si))