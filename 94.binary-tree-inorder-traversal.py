#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        output = []
        if root.left:
            output.extend(self.inorderTraversal(root.left))
        if root.val is not None:
            output.append(root.val)
        if root.right:
            output.extend(self.inorderTraversal(root.right))
        return output

# @lc code=end
