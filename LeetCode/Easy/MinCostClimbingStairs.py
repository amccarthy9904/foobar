# https://leetcode.com/problems/min-cost-climbing-stairs/
# 746. Min Cost Climbing Stairs
# Easy
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if not cost or len(cost) <= 1:
            return 0
            
        # dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        memo = [cost[0], cost[1]]
        
        for i in range(2, len(cost)):
            memo.append(cost[i] + min(memo[i-1], memo[i-2]))
            
        return min(memo[-1], memo[-2])
        
        