# https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/809/
# 322. Coin Change
# Medium
# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Solution 1: Time Limit Exceeded 
# Last executed input:
# [227,99,328,299,42,322]
# 9847
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        v = {}
        
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        
        memo = [(c, 1) for c in coins]
        min_num = sys.maxsize
        
        while memo:
            curr = memo.pop(0)
            
            if curr in v:
                continue
            v[curr] = True
            
            if curr[0] == amount:
                min_num = min(curr[1], min_num)
                continue
            
            if curr[0] > amount or curr[1] >= min_num:
                continue
            
            memo += [(curr[0] + c, curr[1] + 1) for c in coins]
            
        
        if min_num == sys.maxsize:
            return -1
        return min_num

# Sollution 2: Slow Success
# Runtime: 1824 ms, faster than 22.48% of Python3 submissions.
# Memory Usage: 14.6 MB, less than 48.59% of Python3 submissions.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        
        memo = []
          
        d = {}
        for coin in coins:
            d[coin] = True
        
        if 1 in d:
            memo = [1]
        else:
            memo = [-1]
        
        while len(memo) < amount:
            nxt = sys.maxsize
            
            if len(memo)+1 in d:
                memo.append(1)
                continue
            
            for coin in coins:
                
                if coin > len(memo):
                    continue
                
                h = memo[len(memo) - coin]
                
                if h != -1:
                    nxt = min(nxt, h+1)
                    
            if nxt == sys.maxsize:
                memo.append(-1)
            else:
                memo.append(nxt)
                
            
        return memo[-1]