# https://leetcode.com/problems/product-of-array-except-self/description/
# 238. Product of Array Except Self
# Medium
# Given an integer array nums, return an array answer such that
# answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is 
# guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


# Runtime 169ms Beats 57.63% of users with Python3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        pre, post = [1], [1] * l

        [pre.append(nums[i-1] * pre[-1]) for i in range(1, l)]
            
        for i in range(l-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
        
        nums = []
        for i in range(0,l):
            nums.append(post[i] * pre[i])
        
        return nums