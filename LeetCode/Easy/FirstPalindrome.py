# https://leetcode.com/problems/find-first-palindromic-string-in-the-array
# 2108. Find First Palindromic String in the Array
# Easy
# Given an array of strings words, return the first palindromic string in the array.
# If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

class Solution:
    def firstPalindrome(self, wd: List[str]) -> str:

        for w in wd:
            if w == w[::-1]:
                return w
        return ''
        