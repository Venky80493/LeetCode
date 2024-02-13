class Solution:
    def countSubstrings(self, s: str) -> int:
        res=[]
        for i in range(len(s)):
            l,r=i,i
            print(l)
            while l>=0 and r<len(s) and s[l]==s[r]:
                res.append(s[l:r+1])
                l=l-1
                r=r+1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                res.append(s[l:r+1])
                l=l-1
                r=r+1
        return len(res)
            