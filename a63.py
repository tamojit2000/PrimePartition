a=input().split()

m=int(a[0])
s=int(a[1])

max_sum=9*m
min_sum=1

if s>max_sum or s<min_sum:
    print(-1,-1)
    exit()

Max=(10**m-1)-(9*m-s)

Min=int(str(Max)[::-1])

print(Min,Max)
