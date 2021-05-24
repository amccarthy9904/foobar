# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 215. Kth Largest Element in an Array
# Medium

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Solution 1: - not indicitive of most Medium Leetcode problems
# Runtime: 56 ms, faster than 95.48% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15.1 MB, less than 74.14% of Python3 online submissions for Kth Largest Element in an Array.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]