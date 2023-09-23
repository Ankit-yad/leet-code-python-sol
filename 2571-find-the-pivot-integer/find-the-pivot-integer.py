class Solution:
    def pivotInteger(self, n: int) -> int:
        # rightsum=n*(n+1)//2
        rightsum=0
        for i in range(1,n+1):
            rightsum+=i
        leftsum=0
        for i in range(1,n+1):
            rightsum-=i
            if leftsum==rightsum:
                return i
            leftsum+=i
        return -1
        