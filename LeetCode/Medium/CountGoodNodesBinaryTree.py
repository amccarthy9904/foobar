# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# 1448. Count Good Nodes in Binary Tree
# Medium
# Given a binary tree root, a node X in the tree is named good 
# if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# Sol2 - seperated function, use instnace var for count
# Runtime: 244 ms, faster than 71.56% of Python3 online submissions for Count Good Nodes in Binary Tree.
# Memory Usage: 33.5 MB, less than 14.42% of Python3 online submissions for Count Good Nodes in Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root: return 0
        self.count = 0
        self.dfs(root, -sys.maxsize)
        return self.count
    
    def dfs(self, root, lim):
        
        if not root:
            return None
        
        if root.val >= lim:
            self.count += 1
            
        lim = max(root.val,lim)
        self.dfs(root.left, lim)
        self.dfs(root.right, lim)


# Sol 1
# Runtime: 252 ms, faster than 58.88% of Python3 online submissions for Count Good Nodes in Binary Tree.
# Memory Usage: 33.4 MB, less than 62.76% of Python3 online submissions for Count Good Nodes in Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def recur(root, lim):
            
            ret = 0
            
            if not root:
                return 0
            
            if root.val >= lim:
                ret += 1
            
            lim = max(root.val,lim)
            
            ret += recur(root.left, lim)
            ret += recur(root.right, lim)
            
            return ret
        
        return recur(root, -sys.maxsize)