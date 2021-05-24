# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
# 3. Longest Substring Without Repeating Characters
# Medium

# Given a string s, find the length of the longest substring without repeating characters.


# Runtime: 48 ms, faster than 95.98% of Python3 online submissions
# Memory Usage: 14.3 MB, less than 54.28% of Python3 online submissions
class Solution:
    # create empty string new
    # int most
    # loop through s - for c in s
    #   if c in new already
    #        most = max(most, len(new))
    #        slice the front off new to the index after the first c
    #        new = new[:new.index(c)+1:]
    #   add c to new
    # return the max len of new

    def lengthOfLongestSubstring(self, s: str) -> int:
        most, new = 0, ''

        for c in s:
            if c in new:
                most = max(most, len(new))
                new = new[new.find(c) + 1:]
            new += c

        return max(most, len(new))


    def test(self):
        result = self.lengthOfLongestSubstring("abcabcbb")
        print("Result: " + str(result) + "\nExpected: 3")

        result = self.lengthOfLongestSubstring("bbbbb")
        print("Result: " + str(result) + "\nExpected: 1")

        result = self.lengthOfLongestSubstring("pwwkew")
        print("Result: " + str(result) + "\nExpected: 3")


sol = Solution()
sol.test()