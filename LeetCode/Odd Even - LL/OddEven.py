# https://leetcode.com/problems/odd-even-linked-list/
# 328. Odd Even Linked List
# Medium

# Given the head of a singly linked list, group all the nodes with odd indices together 
# followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


            
# Runtime: 40 ms, faster than 81.74% of Python3 online submissions for Odd Even Linked List.
# Memory Usage: 16.5 MB, less than 17.93% of Python3 online submissions for Odd Even Linked List.
class Solution:
    
    
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        even_dummy, odd_dummy = ListNode(), ListNode()
        even_curr, odd_curr = even_dummy, odd_dummy
        
        is_even = False
        
        while head:
            
            curr = head
            head = head.next
            
            if is_even:
                
                even_curr.next = curr
                even_curr = even_curr.next
                even_curr.next = None
            
            else:
                odd_curr.next = curr
                odd_curr = odd_curr.next
                odd_curr.next = None
            
            is_even = not is_even
            
        
        odd_curr.next = even_dummy.next
        return odd_dummy.next
                
            
        