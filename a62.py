x=input().split()

n=int(x[0])
m=int(x[1])
a=int(x[2])
b=int(x[3])

cost1=a
cost2=b/m

if cost1<=cost2:
    print(n*a)

else:
    g=(n//m)*b
    rem=n%m
    d=rem*a
    if d>b:
        g+=b
    else:
        g+=d
    print(g)
    
