# https://leetcode.com/problems/maximum-product-subarray/
# 152. Maximum Product Subarray
# Medium
# Given an integer array nums, find a 
# subarray that has the largest product, 
# and return the product.

# Runtime 63ms Beats 95.69% of users with Python3
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ret = nums[0]
        min_prod = 1
        max_prod = 1

        for num in nums:
            tmp_max = max_prod*num
            tmp_min = min_prod*num
            max_prod = max(tmp_max, tmp_min, num)
            min_prod = min(tmp_max, tmp_min, num)
            ret = max(ret, max_prod, num)
            
        return ret