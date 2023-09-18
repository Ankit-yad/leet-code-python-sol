class Solution:
    def minEatingSpeed(self, v: List[int], h: int) -> int:
        def calculatetotalhours(v,hourly):
            totalh=0
            n=len(v)
            for i in range(n):
                totalh+=math.ceil(v[i]/hourly)
            return totalh
        low=1
        high=max(v)
        while(low<=high):
            mid=(low+high)//2
            totalh=calculatetotalhours(v,mid)
            if totalh <= h:
                high= mid-1
            else:
                low= mid+1
        return low
    # def calculatetotalhours(self, v: List[int], hourly: int) -> int:
    #     totalh=0
    #     n=len(v)
    #     for i in range(n):
    #         totalh+=math.ceil(v[i]/hourly)
    #     return totalh
        