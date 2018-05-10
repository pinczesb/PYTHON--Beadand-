def isPrime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
        return True

def nthPrime(n):
    sum=0
    prime=1
    while sum<n:
        prime+=1
        if isPrime(prime):
            sum+=1
    return prime

print(nthPrime(6))