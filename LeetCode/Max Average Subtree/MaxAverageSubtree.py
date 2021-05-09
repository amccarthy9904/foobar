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






















