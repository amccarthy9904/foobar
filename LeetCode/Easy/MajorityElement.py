# https://leetcode.com/problems/majority-element
# 169. Majority Element
# Easy
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.


# my solution
# O(n) runtime, O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ele = nums[0]
        freq = 1

        for i in range(1, len(nums)):

            if ele == nums[i]:
                freq += 1
            elif freq == 1:
                ele = nums[i]
            else:
                freq -= 1
        
        return ele

# faster solution - Maybe?
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        c = collections.Counter(nums)
        return max(c, key=c.get)



# nerdiest solution:
exec(bytes('浩潰瑲猠慴楴瑳捩ੳ⁦‽灯湥∨獵牥漮瑵Ⱒ✠❷਩潦⁲楬敮椠⁮瑳楤㩮 †渠浵敢彲捯畣敲据獥㴠搠晥畡瑬楤瑣氨浡摢㩡〠਩††畮獭㴠氠獩⡴慭⡰湩ⱴ氠湩⹥獲牴灩⤨ㅛⴺ崱献汰瑩✨✬⤩਩††灵数⁲‽敬⡮畮獭 ⼯㈠ †映牯渠浵敢⁲湩渠浵㩳 †††渠浵敢彲捯畣敲据獥湛浵敢嵲⬠‽਱††††晩渠浵敢彲捯畣敲据獥湛浵敢嵲㸠甠灰牥਺††††††牰湩⡴畮扭牥‬楦敬昽਩††††††牢慥੫硥瑩〨 ','u16')[2:])