# https://leetcode.com/problems/count-and-say/submissions/
# 38. Count and Say
# Medium
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
# which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of groups 
# so that each group is a contiguous section all of the same character. Then for each group, 
# say the number of characters, then say the character. To convert the saying into a digit string, 
# replace the counts with a number and concatenate every saying.



# Sol1:
# Runtime: 52 ms, faster than 34.95% of Python3 submissions
# Memory Usage: 14.3 MB, less than 50.22% of Python3 submissions
class Solution:
    def countAndSay(self, n: int) -> str:
        
        
        if n == 1:
            return "1"
        
        work = self.countAndSay(n-1)
        ret = ""
        temp = []
        
        for c in work:
            temp += c
            
            if  temp[-1] != temp[0]:
                ret += str(len(temp) -1) + str(temp[0])
                temp = [temp[-1]]
            
        ret += str(len(temp)) + str(temp[0])
        return ret
    
# Sol 2: - better
# Runtime: 40 ms, faster than 88.38% of Python3 submissions.
# Memory Usage: 14.2 MB, less than 75.61% of Python3 submissions.
class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        
        work = self.countAndSay(n-1)
        ret = ""
        count = 0
        prev = ""
        
        for c in work:
            
            if count == 0:
                prev = c
            
            elif prev != c:
                ret += str(count) + prev
                prev = c
                count = 0
                
            count += 1
            
        ret += str(count) + prev
        return ret