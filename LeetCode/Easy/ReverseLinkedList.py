# # https://leetcode.com/problems/reverse-linked-list/description/
# 206. Reverse Linked List
# Easy
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next





# from collections import deque
class Solution:
    # this one is better and independent of object data complexity
    def reverseList_while(self, head: [ListNode]) -> [ListNode]:
        
        new_list = None
        current = head
        
        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        return new_list

    def reverseList(self, head: [ListNode]) -> [ListNode]:

        q = []
        start = head
        while head:

            q.append(head.val)
            head = head.next
        
        for val in reversed(q):
            start.val = val
            start = start.next
