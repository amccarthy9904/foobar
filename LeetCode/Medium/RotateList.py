# https://leetcode.com/problems/rotate-list/

# 61. Rotate List
# Medium
# Given the head of a linked list, 
# rotate the list to the right by k places.

# Runtime 37ms Beats 72.86% of users with Python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0 or not head.next:
            return head

        start, l = head, 0

        while head:
            l += 1
            head = head.next

        k = k %  l
        
        if k == 0:
            return start

        d = l - k
        head = start
        
        while d > 1:
            d -= 1
            head = head.next

        new_start = head.next
        head.next = None

        if new_start.next:
            head = new_start.next
            
            while head.next:
                head = head.next
            head.next = start

        else:
            new_start.next = start

        return new_start
