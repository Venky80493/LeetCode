class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        count_dict={}
        for right in range(len(s)):
            count_dict[s[right]]=1+count_dict.get(s[right],0)
            if right-left+1-max(count_dict.values())>k:
                count_dict[s[left]]-=1
                left+=1
        return right-left+1