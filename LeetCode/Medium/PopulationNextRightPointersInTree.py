# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# 117. Populating Next Right Pointers in Each Node II
# Medium
# Given a binary tree
# Populate each next pointer to point to its next right node. 
# If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.


# Runtime: 44 ms, faster than 90.25% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
# Memory Usage: 15.5 MB, less than 7.49% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        stack = [root]
        nxt = []
        
        while stack:
            
            for node in stack:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            
            for n in range(1, len(nxt)):
                nxt[n-1].next = nxt[n]
            stack = nxt
            nxt = []
        
        return root