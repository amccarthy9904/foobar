# https://leetcode.com/problems/candy/
# 135. Candy
# Hard
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

 




# Solution 1: - a little over engineered
# find minima - ind of 1 candy kids
# create cany array , len of ratings, 1s at minima, -1 everyeher else
# from each minima
#     walk left and right as long as rating goes up each step and assign candy vals
#         use max of current candy val and new val 
#     return sum of candy
# Runtime: 180 ms, faster than 33.63% of Python3 online submissions for Candy.
# Memory Usage: 17.2 MB, less than 13.94% of Python3 online submissions for Candy.
class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        if not ratings: return 0
        if len(ratings) == 1: return 1
        
        minima = set()
        candy = []
        
        for ind, r in enumerate(ratings):
            
            if ind == 0:
                if r <= ratings[1]:
                    minima.add(ind)
            
            elif ind == len(ratings)-1:
                if ratings[ind-1] >= r:
                    minima.add(ind)
                
            elif r <= ratings[ind+1] and r <= ratings[ind-1]:
                minima.add(ind)
            
        candy = [1 if ind in minima else -1 for ind in range(len(ratings))]
        
        for mini in minima:
            curr = mini
            
            while curr < len(candy) - 1 and curr+1 not in minima and ratings[curr+1] > ratings[curr]:
                candy[curr+1] = max(candy[curr+1], candy[curr] + 1)
                curr += 1
            
            curr = mini
            while curr > 0 and curr-1 not in minima and ratings[curr-1] > ratings[curr]:
                candy[curr-1] = max(candy[curr-1], candy[curr] + 1)
                curr -= 1
        
        return sum(candy)