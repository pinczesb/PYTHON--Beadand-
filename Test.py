def sumOfFirstN(n,outFile):
    sum = 0
    s=''
    for i in range(1,n+1):
        s += str(i) + '+'
        sum += i
    s = s[0:-1] + '=' + str(sum)
    print(s,file=outFile)
