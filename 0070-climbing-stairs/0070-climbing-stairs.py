class Solution:
    def climbStairs(self, n: int) -> int:
        res=[]
        for i in range(0,n+1):
            if i<2:
                res.append(1)
            else:
                res.append(res[i-1]+res[i-2])
        print(res)
        return res[n]
        # return ref_dict[n-1]