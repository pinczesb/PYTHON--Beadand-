def nthPrime(n):
    L=[]
    for num in range(2,20):
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               L.append(num)
    return L[n-1]

print(nthPrime(6))