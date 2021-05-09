class Solution:
    # create empty string new
    # loop through s - for c in s
    # if c in new already
        # record length of new in most if len is longer than previous max
        # slice the front off new to the index after the first c
    # add c to new
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