# 102. Binary Tree Level Order Traversal
# Medium

# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime: 28 ms, faster than 94.67% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.6 MB, less than 44.42% of Python3 online submissions for Binary Tree Level Order Traversal.

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        ret = [[]]
        curr = [root]
        nxt = []
        
        if not root: return []
        
        while curr:
            
            node = curr.pop(0)
            ret[-1].append(node.val)
            
            if node.left:
                nxt.append(node.left)
            if node.right:
                nxt.append(node.right)
            
            if not curr and nxt:
                curr = nxt
                nxt = []
                ret.append([])
        
        return ret