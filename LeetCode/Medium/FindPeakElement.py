# https://leetcode.com/problems/find-peak-element/
# 162. Find Peak Element
# Medium
# A peak element is an element that is strictly greater than its neighbors.
# Given an integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.
# You must write an algorithm that runs in O(log n) time.

# Sollution 1
# Runtime: 44 ms, faster than 73.70% of Python3 submissions
# Memory Usage: 14.4 MB, less than 70.46% of Python3 submissions

class Solution:
    
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        mid = len(nums) // 2
        
        if mid <= len(nums) - 2 and nums[mid + 1] > nums[mid]:
            return mid + self.findPeakElement(nums[mid:len(nums)])
        
        if mid > 0 and nums[mid - 1] > nums[mid]:
            return self.findPeakElement(nums[0:mid])
        
        return mid

# Slicing the array is non optimal
# The same can be done with a front and back pointer
# Average them to get mid
# Set one equal to mid +- 1
# repeat while front <= back 