# https://leetcode.com/problems/count-special-quadruplets/
# 1995. Count Special Quadruplets
# Easy
# Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
# nums[a] + nums[b] + nums[c] == nums[d], and
# a < b < c < d

# Runtime: 264 ms, faster than 50.00% of Python3 online submissions for Count Special Quadruplets.
# Memory Usage: 14.7 MB, less than 50.00% of Python3 online submissions for Count Special Quadruplets.
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        d = collections.defaultdict(list)
        res = 0
        
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):
                    d[nums[i] + nums[j] + nums[k]].append(k)
        
        for i in range(len(nums)):
            for n in d[nums[i]]:
                if i > n:
                    res += 1
        return res