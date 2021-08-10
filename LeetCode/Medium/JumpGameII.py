# https://leetcode.com/problems/jump-game-ii/
# 45. Jump Game II
# Medium

# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.



# Runtime: 124 ms, faster than 72.91% of Python3 online submissions for Jump Game II.
# Memory Usage: 15.3 MB, less than 55.70% of Python3 online submissions for Jump Game II.
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        max_dist = 0
        steps = 0
        end = 0
        
        for i in range(len(nums) - 1):
            max_dist = max(nums[i] + i, max_dist)
            
            if i == end:
                steps += 1
                end = max_dist
            
        return steps
            