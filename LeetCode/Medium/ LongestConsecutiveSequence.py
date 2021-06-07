# 128. Longest Consecutive Sequence
# Medium
# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Solution1: O(nlogn) time
# Runtime:  200 ms, faster than 33.70% of Python3 submissions
# Memory Usage: 25.9 MB, less than 10.50% of Python3 submissions
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        print(nums)
        prev = nums[0] - 1
        curr_len, max_len = 0, 0
        
        for num in nums:
            
            if num == prev + 1:
                curr_len += 1
                max_len = max(max_len, curr_len)
            
            else:
                curr_len = 1
            
            prev = num
        
        return max_len

# Solution2: O(n)
# Runtime: 180 ms, faster than 43.17% of Python3 submissions
# Memory Usage: 25.7 MB, less than 25.84% of Python3 submissions
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        
        fin = 0
        
        for num in nums:
            
            if num - 1 not in nums:
                start = num
                while start in nums:
                    start += 1
                fin = max(fin, start - num)

        return fin