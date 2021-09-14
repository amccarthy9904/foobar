# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
# 1996. The Number of Weak Characters in the Game
# Medium
# You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

# A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

# Return the number of weak characters.



# Runtime: 3670 ms, faster than 26.17% of Python3 online submissions for The Number of Weak Characters in the Game.
# Memory Usage: 69.3 MB, less than 17.28% of Python3 online submissions for The Number of Weak Characters in the Game.
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1]))
        
        print(properties)
        
        res = 0
        d_max = 0
        
        for a, d in properties:
            
            if d < d_max:
                res += 1
            else:
                d_max = d
                
        return res