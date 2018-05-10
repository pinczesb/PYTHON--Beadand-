"""def Prime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True"""

def nthPrime(n):
    L=[]
    for num in range(2,n + 1):
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               L.append(num)
    return L[-1]

print(nthPrime(6))