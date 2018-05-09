def LCS(x, y):
    if len(x)>len(y):
        max=len(x)
    else:
        max=len(y)
    idx=max-1
    while idx!=-1:
        if len(x) == 0 or len(y) == 0:
           return ""
        if x[idx] == y[idx]:
            return x[idx] + LCS(x[idx+1], y[idx+1])
        else:
            a = LCS(x[idx+1], y)
            b = LCS(x, y[idx+1])

            if len(a) > len(b):
                return a
            else:
                return b

s1='aggtab'
s2='gxtxayb'

print(LCS(s1,s2))
print(len(s1))
print(len(s2))