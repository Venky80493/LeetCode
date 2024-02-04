class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        s_dict={}
        for char in s:
            if char in s_dict.keys():
                s_dict[char]+=1
            else:
                s_dict[char]=1
        t_dict={}
        for char in t:
            if char in t_dict.keys():
                t_dict[char]+=1
            else:
                t_dict[char]=1
        
        return s_dict==t_dict
            