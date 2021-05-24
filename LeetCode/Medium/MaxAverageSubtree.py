# https://leetcode.com/discuss/interview-question/349617
# Given an N-ary tree, find the subtree with the maximum average. Return the root of the subtree.
# A subtree of a tree is the node which have at least 1 child plus all its descendants. The average value of a subtree is the sum of its values, divided by the number of nodes.

# Example 1:

# Input:
# 		 20
# 	   /   \
# 	  12     18
#   /  |  \   / \
# 11   2   3 15  8

# Output: 18
# Explanation:
# There are 3 nodes which have children in this tree:
# 12 => (11 + 2 + 3 + 12) / 4 = 7
# 18 => (18 + 15 + 8) / 3 = 13.67
# 20 => (12 + 11 + 2 + 3 + 18 + 15 + 8 + 20) / 8 = 11.125

# 18 has the maximum average so output 18.


class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    maxSubTree = (None, 0)

    def dfs(self, root : TreeNode):
        total = (root.val, 1)
        if root.children:
            for child in root.children:
                sub = self.dfs(child)
                total = (total[0] + sub[0], total[1] + sub[1])
            avg = total[0] / total[1]
            if avg > self.maxSubTree[1]:
                self.maxSubTree = (root, avg)
        return total

    def max_avg_subtree(self, root : TreeNode) -> TreeNode:
        self.dfs(root)
        return self.maxSubTree[0]



n4 = TreeNode(11, [])
n5 = TreeNode(2, [])
n6 = TreeNode(3, [])
n7 = TreeNode(15, [])
n8 = TreeNode(8, [])
n2 = TreeNode(12, [n4, n5, n6])
n3 = TreeNode(18, [n7, n8])
n1 = TreeNode(20, [n2, n3])
n0 = TreeNode(12, [])
sol = Solution()
print(sol.max_avg_subtree(n1).val)






















