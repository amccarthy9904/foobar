# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
# Medium

# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
# For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

# Given a string n that represents a positive decimal integer, 
# return the minimum number of positive deci-binary numbers needed so that they sum up to n.

# Solution1: Thought it was good
# Time Limit Exceeded

class Solution:
    # loop over digits and construct max db num 
    # subtract from target
    # repeat until target = 0
    # good if need to return the combo of db nums
    # but we only need the quantity of db nums
    def minPartitions(self, n: str) -> int:
        
        count = 0
        
        while int(n) > 0:
            
            nxt_db = 0
            count += 1

            for digit in n:
                
                nxt_db *= 10
                if int(digit) > 0 :
                    nxt_db += 1
                    
            n = str(int(n) - nxt_db)
            
        return count
        # doesnt find the max db number
        # always 0 if it sees digit 0 in n
        # can be 1 if digit greater than 1 has passed 
        # still pretty clean



# Optimal Solution: not as satisfying
# Runtime: 48 ms, faster than 89.73% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
# Memory Usage: 14.7 MB, less than 83.88% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
class Solution:
    def minPartitions(self, n: str) -> int:
        
        return max(n)