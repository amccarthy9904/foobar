# https://leetcode.com/problems/add-two-numbers/
# 2. Add Two Numbers
# Medium
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# First Try: - ok solution but not very clever
# Runtime: 76 ms, faster than 22.47% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.3 MB, less than 71.52% of Python3 online submissions for Add Two Numbers.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def get_num(head):
            if head.next:
                return head.val + 10 * get_num(head.next)
            else:
                return head.val
            
        num_list = [int(dig) for dig in str(get_num(l1) + get_num(l2))]
        
        dummy = ListNode()
        curr = ListNode()
        dummy.next = curr
        
        while num_list:
            curr.val = num_list.pop()
            if num_list:
                temp = ListNode()
                curr.next = temp
                curr = temp
            
        return dummy.next


# Second Try: - more elegant, not terribly faster tho
# Runtime: 72 ms, faster than 47.84% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.4 MB, less than 42.68% of Python3 online submissions for Add Two Numbers.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c = 0) -> ListNode:
        
        val = l1.val + l2.val + c
        c2 = val // 10
        ret = ListNode( val % 10 )
        
        if l1.next or l2.next or c2 != 0:
            
            if not l1.next:
                l1.next = ListNode()
            if not l2.next:
                l2.next = ListNode()
            
            ret.next = self.addTwoNumbers(l1.next, l2.next, c2)
        
        return ret         