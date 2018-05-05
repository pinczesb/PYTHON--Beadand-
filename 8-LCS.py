def LongestCommonSubsequence(str1,str2):
    idx=0
    lcs=""
    if len(str1)>len(str2):
        maxlen=str1
    if len(str1)<len(str2):
        maxlen=str2
    else:
        maxlen=str1
    while idx<len(maxlen):
        if str1[idx] is str2[idx]:
            lcs+=maxlen[idx]
        return lcs
    idx+=1


s1="aaafghl"
s2="aaakgh"
print(LongestCommonSubsequence(s1,s2))