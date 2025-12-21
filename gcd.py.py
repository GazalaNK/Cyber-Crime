from math import gcd
def RSA(p:int,q:int,msg:int):
    n=p*q
    t=(p-1)*(q-1)
    for i in range(2,t):
        if gcd(i,t)==1:
            e=i
            break
    j=0
    while True:
        if (j*e)%t==1:
            d=j
            break
        j+=11
    ct=(msg**e)%n
    print(ct,"\n")
    mes=(ct**d)%n
    print(mes,"\n")
RSA(p=53,q=59,msg=89)
RSA(p=3,q=7,msg=12)
