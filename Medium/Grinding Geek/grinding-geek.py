
from typing import List
import math

class Solution:
    def max_courses(self, n: int, total: int, cost: List[int]) -> int:
        def f(i, total, cost, dp):
            if i == n or total <= 0:
                return 0

            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = max(1 + f(i + 1, math.floor(total - (10 / 100 * cost[i])), cost, dp) if cost[i] <= total else 0,
                                f(i + 1, total, cost, dp))

            return dp[(i, total)]

        dp = {}
        return f(0, total, cost, dp)

        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        total = int(input())
        
        
        cost=IntArray().Input(n)
        
        obj = Solution()
        res = obj.max_courses(n, total, cost)
        
        print(res)
        

# } Driver Code Ends