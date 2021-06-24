# https://leetcode.com/problems/validate-binary-search-tree/
# 98. Validate Binary Search Tree
# Medium
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Solution 1: pretty good
# Runtime: 36 ms, faster than 96.89% of Python3 submissions
# Memory Usage: 16.4 MB, less than 79.34% of Python3 submissions

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def search(root, ma, mi):
            
            if not root: return True
            
            if root.val >= ma or root.val <= mi:
                return False
            
            return search(root.left, root.val, mi) and search(root.right, ma, root.val)
        
        return search(root, sys.maxsize, -sys.maxsize)