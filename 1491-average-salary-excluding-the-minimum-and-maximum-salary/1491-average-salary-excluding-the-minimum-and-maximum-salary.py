class Solution:
    def average(self, salary: List[int]) -> float:
        min=salary[0]
        max=salary[0]
        sum=0
        for i in range(0,len(salary)):
            if min>salary[i]:
                min=salary[i]
            if max<salary[i]:
                max=salary[i]
            sum+=salary[i]
        return (sum-min-max)/(len(salary)-2)