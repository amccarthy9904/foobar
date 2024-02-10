# https://leetcode.com/problems/rotate-array/submissions/1171707495/
# 189. Rotate Array
# Medium
# Given an integer array nums, 
# rotate the array to the right by k steps, 
# where k is non-negative.

# O(n)
# Runtime 153 ms Beats 86.44% of users with Python3
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l 
        nums[:] = nums[l - k : l] + nums[:l - k]
# O(n)
# Runtime 176ms Beats 37.56% of users with Python3
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(arr, i, j):

            while i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1
            print(arr)

        l = len(nums)
        k = k % l
        reverse(nums, 0, l - k - 1)
        reverse(nums, l - k, l - 1)
        reverse(nums, 0, l - 1)