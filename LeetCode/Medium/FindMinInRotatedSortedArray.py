# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# 153. Find Minimum in Rotated Sorted Array
# Medium
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Runtime 34ms Beats 96.63% of users with Python3
class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) -1
        mid = (l + r) // 2
        while nums[mid] > nums[(mid+1)%len(nums)] or nums[mid] > nums[mid-1]:
            
            if nums[mid] > nums[r]:
                l = mid
                mid = (mid + r) // 2 + 1
            elif nums[mid] < nums[l]:
                r = mid
                mid = (mid + l) // 2
            else:
                mid -= 1

        return nums[mid]

