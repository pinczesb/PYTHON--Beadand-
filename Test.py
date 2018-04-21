def sumOfFirstN(n,outFile):
    sum = 0
    s=''
    for i in range(1,n+1):
        s += str(i) + '+'
        sum += i
    s = s[0:-1] + '=' + str(sum)
    print(s,file=outFile)

def secondsToTime(n,outFile):
    tmp = n
    year = n//(3600*24*365)
    n=n%(3600*24*365)
    day = n//(3600*24)
    n = n%(3600*24)
    hour = n//3600
    n = n%3600
    min = n//60
    sec = n%60
    print('{} seconds is {} year {} day {} hours {} minutes and {} seconds'.format(tmp,year,day,hour,min,sec))

def sumOfNumbers(outFile):
    sum = 0;
    for n in outFile:
        sum+=int(n)
    return sum

def sumOfFirstN(n,outFile):
    sum = 0
    s=''
    for i in range(1,n+1):
        s += str(i) + '+'
        sum += i
    s = s[0:-1] + '=' + str(sum)
    print(s,file=outFile)
