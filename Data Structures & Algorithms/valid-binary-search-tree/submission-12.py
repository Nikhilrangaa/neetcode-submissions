class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        def dfs(node, lower, upper):
            if node is None:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, float("-inf"), float("inf"))