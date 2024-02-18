class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        mx_len=0
        charSet=set()
        for right in range(len(s)):
            if s[right] not in charSet:
                charSet.add(s[right])
                mx_len=max(mx_len,right-left+1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left+=1
                charSet.add(s[right])
        return mx_len
                
            