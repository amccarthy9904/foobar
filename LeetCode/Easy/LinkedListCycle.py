# https://leetcode.com/problems/linked-list-cycle/
# 141. Linked List Cycle
# Easy
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that 
# can be reached again by continuously following the next pointer. 
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime 36ms Beats 96.76% of users with Python3
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        behind = head
        head = head.next
        slow = False
        
        while head:
            
            if head == behind:
                return True
            head = head.next
            
            if slow:
                behind = behind.next
                slow = False
            else:
                slow = True
        
        return False
        