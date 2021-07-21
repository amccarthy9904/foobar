# https://leetcode.com/problems/shuffle-an-array
# 384. Shuffle an Array
# Medium

# Given an integer array nums, design an algorithm to randomly shuffle the array. 
# All permutations of the array should be equally likely as a result of the shuffling.

# Implement the Solution class:

# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.
 

import random

class Solution:

    nums = []
    
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        
    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        temp = [i for i in range(len(self.nums))]
        rand = []
        
        while temp:
            rand.append(self.nums[temp.pop(random.randrange(len(temp)))])
        return rand
        
        
        