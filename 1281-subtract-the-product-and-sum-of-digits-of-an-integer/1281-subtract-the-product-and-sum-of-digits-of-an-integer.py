class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits=len(str(n))
        product=1
        sum=0
        for i in range(0,digits):
            product*=int(str(n)[i])
            sum+=int(str(n)[i])
        return product-sum