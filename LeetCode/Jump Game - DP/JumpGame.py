# 55. Jump Game
# Medium
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.



# Solution 1:
# Runtime: 108 ms, faster than 8.72% of Python3 online submissions for Jump Game.
# Memory Usage: 18.3 MB, less than 5.73% of Python3 online submissions for Jump Game.

class Solution:
    def canJump(self, nums) -> bool:
        
        max_jump = 0
        memo = [0]
        visited = {}
        while memo:
            
            curr = memo.pop()
            if curr in visited:
                continue
            visited[curr] = True
            max_jump = max(max_jump, curr + nums[curr])
            
            if max_jump >= len(nums) - 1:
                return True
            
            if nums[curr] + curr < max_jump:
                continue 
                
            memo += [n for n in range(curr+1, curr+nums[curr] + 1) if n not in visited]
        
        return False
        
# Solution 2, better, still not amazing
# Runtime: 88 ms, faster than 59.46% of Python3 online submissions for Jump Game.
# Memory Usage: 16.1 MB, less than 50.37% of Python3 online submissions for Jump Game.

class Solution:
    def canJump(self, nums) -> bool:
        
        max_jump = 0
        
        for i in range(0, len(nums) - 1):
            
            if i > max_jump:
                return False    
            max_jump = max(max_jump, i + nums[i])
            
        return max_jump >= len(nums) - 1
        