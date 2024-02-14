# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 33. Search in Rotated Sorted Array
# Medium
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.

# Runtime 46ms Beats 50.38% of users with Python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) -1
        while l <= r:

            m = (l + r) // 2
            print(f"m{m}")
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1
        

# Solution: not great, shouldnt need to check l r and m
# Runtime: 40 ms, faster than 74.72% of Python3 submissions
# Memory Usage: 14.8 MB, less than 20.45% of Python3 submissions 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
        
        l = 0
        r = len(nums) - 1
        m = len(nums) // 2
        
        
        done = False
        while not done:
            
            if nums[m] == target:
                return m
            if nums[r] == target:
                return r
            if nums[l] == target:
                return l
            
            if nums[l] > nums[m]:
                #axis between l and m
                if target > nums[l] or target < nums[m]:
                    r = m
                else:
                    l = m
                
            elif nums[r] < nums[m]:
                #axis between m and r
                if target > nums[m] or target < nums[r]:
                    l = m
                else:
                    r = m
            else:
                #axis outside l and r
                if target > nums[m]:
                    l = m
                else:
                    r = m
                    
            temp = m
            m = (l + r) // 2
            
            if temp == m:
                return -1
        