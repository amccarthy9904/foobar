# https://leetcode.com/problems/contains-duplicate
# 217. Contains Duplicate
# Solved
# Given an integer array nums, return true 
# if any value appears at least twice in the array, 
# and return false if every element is distinct.

# end when duplicate is found instead of createing the entire set
# Runtime 413ms Beats 86.95% of users with Python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        s = set()
        for num in nums:
            if num in s: return True
            s.add(num)
        return False
        
# create entire set
# Runtime 422ms Beats 68.32% of users with Python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(set(nums)) != len(nums)
    

        