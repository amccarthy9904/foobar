# https://leetcode.com/problems/rearrange-array-elements-by-sign

# 2149. Rearrange Array Elements by Sign
# Medium

# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should rearrange the elements of nums such that the modified array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

# everyone else just made a new array and returned that which is a little bit faster

from collections import deque
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pq, nq = deque(), deque()

        for r in range(len(nums)):

            tmp = nums[r]
            if tmp > 0:
                pq.append(tmp)
            else:
                nq.append(tmp)
        
        for i in range(len(nums)):

            if i % 2 == 0:
                nums[i] = pq.popleft()
            else:
                nums[i] = nq.popleft()
        return nums