# https://leetcode.com/problems/construct-target-array-with-multiple-sums/
# 1354. Construct Target Array With Multiple Sums
# Hard
# 
# You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :
# 
# let x be the sum of all elements currently in your array.
# choose index i, such that 0 <= i < n and set the value of arr at index i to x.
# You may repeat this procedure as many times as needed.
# Return true if it is possible to construct the target array from arr, otherwise, return false.

# Solution 1 - Time Limit Exceeded
# TODO: revisit this
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        A = [1] * len(target)
        
        done = False
        
        while not done:
            
            if A == target:
                return True
            
            ind = target.index(max(target))
            diff = target[ind] - max(target[:ind] + target[ind+1:])
            delta = (sum(target) - target[ind])
            
            
            target[ind] = target[ind] - delta * (diff//delta)
            print(target)
            if min(target) < 1:
                return False
        
        return False
        