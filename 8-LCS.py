def LCS(s1,s2):
    if len(s1)==0 or len(s2)==0:
       return ""
    if s1[0]==s2[0]:
        return s1[0]+LCS(s1[1:],s2[1:])
    else:
        a=LCS(s1[1:],s2)
        b=LCS(s1,s2[1:])
        if len(a)>len(b):
            return a
        else:
            return b

#s1='aggtab'
#s2='gxtxayb'
s1='abe'
s2='bea'
print(LCS(s1,s2))
