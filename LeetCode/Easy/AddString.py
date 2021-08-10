# https://leetcode.com/problems/add-strings/submissions/
# 415. Add Strings
# Easy
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.



# Runtime: 44 ms, faster than 56.67% of Python3 online submissions for Add Strings.
# Memory Usage: 14.3 MB, less than 64.52% of Python3 online submissions for Add Strings.
class Solution:
    
    def get_dig(self, num, digit):
        
        try:
            return int(num[digit])
        except:
            return 0
    
    def addStrings(self, num1: str, num2: str) -> str:
              
        num_sum = ''
        carry = 0
        digit = -1
        stop = max(len(num1), len(num2))
        
        while -(digit) < stop+1:
            
            dig_sum = self.get_dig(num1, digit) + self.get_dig(num2, digit) + carry
            carry = 0
            digit -= 1
            
            if dig_sum >= 10:
                dig_sum -= 10
                carry = 1
                
            num_sum = str(dig_sum) + num_sum
        
        if carry:
            return '1' + num_sum
        else:
            return num_sum