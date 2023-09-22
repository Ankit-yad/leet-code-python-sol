class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s=sum(nums)
        l=s-nums[-1]
        r=nums[-1]
        c=0
        n=len(nums)-1
        for i in range(n-1,-1,-1):
            if l>=r:
                c+=1
            l-=nums[i]
            r+=nums[i]
        return c
        