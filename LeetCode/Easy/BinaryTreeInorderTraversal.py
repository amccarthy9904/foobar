# https://leetcode.com/problems/binary-tree-level-order-traversal
# 94. Binary Tree Inorder Traversal
# Easy
# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Runtime: 32 ms, faster than 52.92% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 13.9 MB, less than 98.46% of Python3 online submissions for Binary Tree Inorder Traversal.
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        ret = []
        
        if not root: return ret
        
        if root:
            ret += self.inorderTraversal(root.left)
        
        ret += [root.val]
        
        if root:
            ret += self.inorderTraversal(root.right)
            
        return ret
        