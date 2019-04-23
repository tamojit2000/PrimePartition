def isprime(num):
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    else:
        return True


def primepartition(m):
    if m<0:
        return False
    elif m%2 == 0 and m>2:
        return True
    elif (m-1)%2==0 and isprime(m-2):
        return True
    else:
        return False

x=int(input("Enter a number: "))
print(primepartition(x))
