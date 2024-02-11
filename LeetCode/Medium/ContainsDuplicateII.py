# https://leetcode.com/problems/contains-duplicate-ii/
# 219. Contains Duplicate II
# Easy
# Given an integer array nums and an integer k 
# return true if there are two distinct indices 
# i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# O(n)
# by defining our window set to be all values whose indicies satisfy abs(i - j) <= k
# upon finding a match we return True
# Runtime 454ms Beats 87.43% of users with Python3
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        win = set()
        l = 0

        for r, num in enumerate(nums):
            if r > k:
                win.remove(nums[l])
                l+=1
            
            if num in win:
                return True
            
            else:
                win.add(num)

        return False