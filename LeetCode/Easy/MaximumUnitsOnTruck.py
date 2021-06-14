# https://leetcode.com/problems/maximum-units-on-a-truck/
# 1710. Maximum Units on a Truck
# Easy
# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, 
# where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes 
# that can be put on the truck. You can choose any boxes to put on the truck 
# as long as the number of boxes does not exceed truckSize.

# # Return the maximum total number of units that can be put on the truck.
# O(nlogn)
# Runtime: 148 ms, faster than 90.39% of Python3 online submissions for Maximum Units on a Truck.
# Memory Usage: 14.6 MB, less than 89.23% of Python3 online submissions for Maximum Units on a Truck.
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxes = sorted(boxTypes, key=lambda box: box[1])
        
        loaded = 0
        
        while truckSize > 0 and boxes:
            
            box = boxes.pop()
            
            to_load = min(box[0], truckSize)
            loaded += to_load * box[1]
            truckSize -= to_load
        
        return loaded
            