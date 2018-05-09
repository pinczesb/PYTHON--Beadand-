def lcs(x, y):
    for idx1 in range(len(x)-1):
        for idx2 in range(len(y)-1):
            if len(x) == 0 or len(y) == 0:
               return ""
            if x[idx1] == y[idx2]:
                return x[idx1] + lcs(x[idx1], y[idx2])
            else:
                a = lcs(x[idx1], y)
                b = lcs(x, y[idx2])
                if len(a) > len(b):
                    return a
                else:
                    return b

s1='aggtab'
s2='gxtxayb'

print(lcs(s1,s2))
print(len(s1))
print(len(s2))
s1='aggtab'
s2='gxtxayb'

print(LCS(s1,s2))
print(len(s1))
print(len(s2))