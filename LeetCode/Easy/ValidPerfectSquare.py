# https://leetcode.com/problems/valid-perfect-square/
# 367. Valid Perfect Square
# Easy
# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. In other words, 
# it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.

# Runtime 30ms Beats 89.49% of users with Python3
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        done = False
        l, r = 0, num
        while l <= r:
            
            m = (l + r) // 2
            guess = m * m
            if guess == num:
                return True
            
            if guess < num:
                l = m + 1
            else:
                r = m - 1
        return False