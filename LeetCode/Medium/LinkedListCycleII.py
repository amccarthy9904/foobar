# https://leetcode.com/problems/linked-list-cycle-ii/submissions/
# 142. Linked List Cycle II
# Medium

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by 
# continuously following the next pointer. Internally, pos is used to denote the index of the node that 
# tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Notice that you should not modify the linked list.


# Runtime: 40 ms, faster than 98.21% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 17.2 MB, less than 55.46% of Python3 online submissions for Linked List Cycle II.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        d = {}
        
        while head:
            
            if head in d:
                return head
            
            d[head] = True
            head = head.next
            
        return None
        