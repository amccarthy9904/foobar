# https://leetcode.com/problems/array-of-doubled-pairs/
# 954. Array of Doubled Pairs
# Medium
# Given an array of integers arr of even length, return true if and only if 
# it is possible to reorder it such that arr[2 * i + 1] = 2 * arr[2 * i] 
# for every 0 <= i < len(arr) / 2.

# Solution 2
# Runtime: 556 ms, faster than 97.13% of Python3 online submissions for Array of Doubled Pairs.
# Memory Usage: 16.6 MB, less than 58.85% of Python3 online submissions for Array of Doubled Pairs.
import collections

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        # hash table keeps track of count of each element in arr
        # value in arr : quantity of that value
        count = collections.Counter(arr)
        
        for x in sorted(count, key=abs):
            
            # there must be at least as many 2's as 1's
            # else the 1's will not have pairs
            if count[x] > count[x*2]:
                return False
            
            # there are now less 2's open to pair with 4's
            count[x*2] -= count[x]
            
        return True


# Solution 1
# Runtime: 684 ms, faster than 62.68% of Python3 online submissions for Array of Doubled Pairs.
# Memory Usage: 17.1 MB, less than 6.22% of Python3 online submissions for Array of Doubled Pairs.
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        d = {}
        pairs = []
        arr.sort(key=abs)
        
        for num in arr:
            
            if num in d:
                
                pairs.append([num, d[num][0]])
                if d[num][1] > 1:
                    d[num][1] -= 1
                else:
                    del d[num]
            
            else:
                if num*2 in d:
                    d[num*2][1] += 1
                else:
                    d[num*2] = [num, 1]
                
        return len(pairs) * 2 == len(arr)