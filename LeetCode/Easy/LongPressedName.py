# https://leetcode.com/problems/long-pressed-name/
# 925. Long Pressed Name
# Easy
# Your friend is typing his name into a keyboard. Sometimes, when typing a character c,
# the key might get long pressed, and the character will be typed 1 or more times.

# You examine the typed characters of the keyboard. Return True if it is possible 
# that it was your friends name, with some characters (possibly none) being long press

# Runtime: 28 ms, faster than 85.87% of Python3 online submissions for Long Pressed Name.
# Memory Usage: 14.4 MB, less than 31.44% of Python3 online submissions for Long Pressed Name.
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        if not name and typed:
            return False
        
        name = [c for c in name]
        typed = [c for c in typed]
        seen = set()
        c = ''
        try:
            while name:

                c = name.pop(0)

                t = typed.pop(0)
                if c not in seen:
                    seen.add(c)

                if t != c:

                    if t not in seen:
                        return False

                    ind = typed.index(c)

                    for i in range(ind):
                        if typed.pop(0) != t:
                            return False
                    typed.pop(0)  

        except:
            return False
        
        for i in range(len(typed)):
            if typed[i] != c:
                return False
        
        return True