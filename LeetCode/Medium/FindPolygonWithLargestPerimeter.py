# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter
# 2971. Find Polygon With the Largest Perimeter
# Medium
# You are given an array of positive integers nums of length n.

# A polygon is a closed plane figure that has at least 3 sides. 
# The longest side of a polygon is smaller than the sum of its other sides.

# Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak 
# where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, 
# then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

# The perimeter of a polygon is the sum of lengths of its sides.

# Return the largest possible perimeter of a polygon whose sides can be formed from nums, 
# or -1 if it is not possible to create a polygon.

# Runtime 501ms Beats 89.55% of users with Python3
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums = sorted(nums)
        s = sum(nums)

        for i in range(len(nums)-1, 1, -1):

            big = nums[i]
            s -= big
            if s > big:
                return s + big
        
        return -1

# heapq version
# Runtime 457ms Beats 98.87% of users with Python3
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        curr = sum(nums)
        heapq._heapify_max(nums)
        while nums and curr <= nums[0] * 2:
            curr -= heapq._heappop_max(nums)
        return curr if len(nums) > 2 else -1